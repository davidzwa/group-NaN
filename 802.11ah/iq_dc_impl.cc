/*
 * Copyright 2018 Danilo Verhaert <daniloverhaert@gmail.com>.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#include "iq_dc_impl.h"

#include <gnuradio/io_signature.h>
#include <boost/format.hpp>

namespace gr {
namespace foo {

iq_dc_impl::iq_dc_fix_impl(void) : gr::block("iq_dc_fix",
gr::io_signature::make(1, 1, sizeof(gr_complex)),
gr::io_signature::make(1, 1, sizeof(gr_complex)))
{
    float real_average =0.0;
    float imaginary_average = 0.0;
    float ratio=1e-05f;
}

iq_dc_impl::~iq_dc_impl() {}

iq_dc_fix_impl:: work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items) {
					   
    for (int i = 0; i < noutput_items; i++)	{
        real_average = real_average + ratio * (in[i].real() - real_average);
      	imaginary_average = imaginary_average + ratio * (in[i].imag() - imaginary_average);

        out[i] = gr_complex(in[i].real() - real_average, in[i].imag() - imaginary_average);
      	}
		return noutput_items;
	}
} /* namespace foo */
} /* namespace gr */
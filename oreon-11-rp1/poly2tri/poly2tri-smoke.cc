// SPDX-License-Identifier: BSD-3-Clause
//
// Minimal headless smoke test for the packaged poly2tri library.

#include <cstddef>
#include <iostream>
#include <vector>

#include <poly2tri/poly2tri.h>

int main()
{
    std::vector<p2t::Point*> polyline;
    polyline.push_back(new p2t::Point(0.0, 0.0));
    polyline.push_back(new p2t::Point(1.0, 0.0));
    polyline.push_back(new p2t::Point(1.0, 1.0));
    polyline.push_back(new p2t::Point(0.0, 1.0));

    std::size_t triangle_count = 0;
    {
        p2t::CDT cdt(polyline);
        cdt.Triangulate();
        triangle_count = cdt.GetTriangles().size();
    }

    for (std::vector<p2t::Point*>::iterator it = polyline.begin();
         it != polyline.end(); ++it) {
        delete *it;
    }

    std::cout << "triangles=" << triangle_count << " (expected 2)" << std::endl;
    return triangle_count == 2 ? 0 : 1;
}

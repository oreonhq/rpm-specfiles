%global source0_hash a14320d82194807c4480ce59c98aa71cd4175a5156645c4e2b3edd330b930627
Name:           polyclipping
Version:        6.4.2
Release:        1%{?dist}
%global so_version 22
Summary:        Polygon clipping library
License:        BSL-1.0
URL:            https://sourceforge.net/projects/polyclipping
Source0:        https://downloads.sourceforge.net/%{name}/clipper_ver%{version}.zip
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1

# Delete binaries
find . \( -name "*.exe" -o -name "*.dll" \) -delete

# Delete bundled(js-syntaxhighlighter),
# https://github.com/syntaxhighlighter/syntaxhighlighter.
rm -rvf Documentation/Scripts/SyntaxHighlighter

# Correct line ends and encodings
find . -type f -exec dos2unix -k {} \;

for filename in "Third Party/perl/perl_readme.txt" README; do
  iconv -f iso8859-1 -t utf-8 "${filename}" > "${filename}".conv && \
    touch -r "${filename}" "${filename}".conv && \
    mv "${filename}".conv "${filename}"
done

%build

pushd cpp
  export CMAKE_POLICY_VERSION_MINIMUM='3.12'
  %cmake %["%{?_lib}" == "lib64" ? "-DLIB_SUFFIX=64" : ""]
  %cmake_build
popd
%install
pushd cpp
  %cmake_install
  sed -e 's/\.\.\/clipper\.hpp/clipper.hpp/' < cpp_agg/agg_conv_clipper.h > %{buildroot}/%{_includedir}/%{name}/agg_conv_clipper.h
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n polyclipping-devel -f %{oreon_filedir}/polyclipping-devel.list

%changelog

%autochangelog

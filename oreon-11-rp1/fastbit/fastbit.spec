%global source0_hash 1ddb16d33d869894f8d8cd745cd3198974aabebca68fa2b83eb44d22339466ec

Name:           fastbit
Version:        2.0.3
Release:        34%{?dist}
Summary:        An Efficient Compressed Bitmap Index Technology
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://sdm.lbl.gov/fastbit/
Source0:        https://code.lbl.gov/frs/download.php/file/426/%{name}-%{version}.tar.gz

# Code patch to fix format truncation issue, sent to upstream ML
Patch0:         fastbit_format_truncation.patch

# Code patch to fix FSF address in fbmerge.cpp, sent to upstream ML
Patch1:         fastbit_fsf_address.patch

# Code patch to remove indentation warnings, sent to upstream ML
Patch2:         fastbit_indentation.patch

# Code patch to remove unused variable warnings, sent to upstream ML
Patch3:         fastbit_unused_variable.patch

# Build system patch to ensure linkage to pthread
Patch10:        fastbit_pthread_linkage.patch

# Build system patch for tests to use compiled binaries, not libtool wrappers
Patch11:        fastbit_tests_use_binaries.patch

Patch30:        %{name}-gcc11.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-interpreter

%description
FastBit is an open-source data processing library following the spirit of NoSQL
movement. It offers a set of searching functions supported by compressed bitmap
indexes. It treats user data in the column-oriented manner similar to
well-known database management systems such as Sybase IQ, MonetDB, and Vertica.
It is designed to accelerate user's data selection tasks without imposing undue
requirements.

%package devel
Summary: FastBit development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development package for FastBit.  Includes headers, libraries and man pages for
using FastBit API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

echo fixing permissions ...
find . -type f -perm /0111 \
    \( -name \*.cpp -or -name \*.h -or -name \*.yy -or -name \*.ll -or \
       -name \*.html -or -name README \) -print -exec chmod 0644 {} \;

%build
aclocal -I tests/m4
autoconf
automake --copy --no-force
%configure \
    --disable-static \
    --enable-contrib \
    --with-quiet-nan
# patch libtool to remove rpaths
sed -i 's|^hardcode_into_libs=.*|hardcode_into_libs=no|g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%check
# The test binaries need LD_LIBRARY_PATH to find the compiled fastbit library
# in the build tree.
%make_build LD_LIBRARY_PATH="%{buildroot}%{_libdir};%{_libdir}" check

%install
%make_install

# remove libtool archives
find %{buildroot} -name \*.la | xargs rm -f

%ldconfig_scriptlets
%ldconfig_scriptlets -n devel

%files
%doc NEWS README
%license COPYING
%{_docdir}/%{name}/*.html
%{_bindir}/ardea
%{_bindir}/fbmerge
%{_bindir}/ibis
%{_bindir}/rara
%{_bindir}/tcapi
%{_bindir}/thula
%{_bindir}/tiapi
%{_libdir}/libfastbit.so.*

%files devel
%dir %{_prefix}/include/%{name}
%{_prefix}/include/%{name}/*.{h,hh}
%{_bindir}/fastbit-config
%{_libdir}/libfastbit.so

%changelog
%autochangelog

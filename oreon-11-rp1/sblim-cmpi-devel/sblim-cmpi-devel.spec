
Name:           sblim-cmpi-devel
Version:        2.0.3
Release:        34%{?dist}
Summary:        SBLIM CMPI Provider Development Support

License:        EPL-1.0
URL:            http://sblim.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
# Source1: macro definitions
Source1: macros.sblim-cmpi-devel

# Patch0:       remove version from docdir
Patch0:         sblim-cmpi-devel-2.0.3-docdir.patch
# oreon url source checksums begin
%global source0_sha256 1671cabff6b922b6fde897673d9fdafd56c9310f82a7eacc0547d596b9cdfea6
%global source0_file sblim-cmpi-devel-2.0.3.tar.bz2
# oreon url source checksums end
BuildRequires: make
BuildRequires:  gcc


%description
This packages provides the C and C++ CMPI header files needed by
provider developers and can be used standalone. If used for
C++ provider development it is also necessary to have
tog-pegasus-devel installed.

%package -n libcmpiCppImpl0
License:        EPL-1.0
Summary:        CMPI C++ wrapper library
Conflicts:      tog-pegasus-libs
BuildRequires:  gcc-c++

%description -n libcmpiCppImpl0
This packages provides the C++ wrapper library for CMPI development

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/sblim-cmpi-devel-2.0.3.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "1671cabff6b922b6fde897673d9fdafd56c9310f82a7eacc0547d596b9cdfea6" || { echo "oreon: Source0 SHA256 mismatch for sblim-cmpi-devel-2.0.3.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
%patch -P0 -p1 -b .docdir

%build
%configure
%make_build

%install
%make_install
# remove unused libtool files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a
# install macro definitions
mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d
cp %{SOURCE1} $RPM_BUILD_ROOT%{_rpmconfigdir}/macros.d

%ldconfig_scriptlets -n libcmpiCppImpl0

%files
%doc AUTHORS COPYING README
%{_includedir}/cmpi
%{_rpmconfigdir}/macros.d/macros.sblim-cmpi-devel

%files -n libcmpiCppImpl0
%{_libdir}/libcmpiCppImpl.so*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.3-34
- Prepare for Oreon 11 (RP1)

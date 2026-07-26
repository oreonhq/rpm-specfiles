%global source0_hash cbbba395d2425251263e4ae05c4829319a3e399a0aee70df2eb9efb6a8afdbae

Name:           aces_container
Version:        1.0.2
Release:        %autorelease
Summary:        ACES Container Reference

License:        AMPAS
URL:            https://github.com/ampas/aces_container
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         Switch-to-CMAKE-default-variables.patch
Patch1:         Set-the-appropriate-SONAME-for-the-library.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
This folder contains a reference implementation for an ACES container
file writer intended to be used with the Academy Color Encoding
System (ACES). The resulting file is compliant with the ACES container
specification (SMPTE S2065-4). However, there are a few things that are
not demonstrated by this reference implementation.

    Stereo channels
    EndOfFileFiller
    Arbitrary attributes and naming validations
    half type attributes
    keycode value validations

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod -x aces_writeattributes.*

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake

%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/libAcesContainer.so.*

%files devel
%dir %{_includedir}/aces/
%{_includedir}/aces/*.h
%dir %{_libdir}/cmake/AcesContainer
%{_libdir}/cmake/AcesContainer/*.cmake
%{_libdir}/libAcesContainer.so
%{_libdir}/pkgconfig/AcesContainer.pc

%changelog
%autochangelog

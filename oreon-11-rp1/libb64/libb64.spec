%global source0_hash 343d8d61c5cbe3d3407394f16a5390c06f8ff907bd8d614c16546310b689bfd3

Name:           libb64
Version:        1.2
Release:        19%{?dist}
Summary:        Tools for fast encoding/decoding data into and from a base64-encoded format

License:        LicenseRef-Fedora-Public-Domain
URL:            http://libb64.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.zip

BuildRequires: gcc-c++
BuildRequires: make

%description
Base64 uses a subset of displayable ASCII characters, and is therefore a useful
encoding for storing binary data in a text file, such as XML, or sending binary
data over text-only email.

libb64 is a library of ANSI C routines for fast encoding/decoding data into and
from a base64-encoded format. C++ wrappers are included, as well as the source
code for standalone encoding and decoding executables.

%package        devel
Summary:        Development files for %{name}
# Upstream only provides a static library
Provides:      %{name}-static = %{version}-%{release}
# Does not need to require the base package as it is complete itself

%description    devel
The %{name}-devel package contains the library and header files for developing
applications that use %{name}.

%package tools
Summary:        %{name}-b64 binary provided by %{name}

%description tools
This package provides the %{name}-b64 binary tool for encoding to and decoding
from the Base64 scheme. Please install the %{name}-devel package to develop
software using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Remove unneeded flags
sed -i '/-O3/ d' src/Makefile
sed -i '/pedantic/ d' src/Makefile

%build
%set_build_flags
%make_build

%install
# Upstream doesn't provide any install bits in the Makefile
# static lib
install -D -m 0644 -p src/libb64.a $RPM_BUILD_ROOT/%{_libdir}/libb64.a
# binary, rename to prevent conflict with coreutils binary
install -D -m 0755 -p base64/base64 $RPM_BUILD_ROOT/%{_bindir}/libb64-base64
# headers
install -D -m 0644 -p -t $RPM_BUILD_ROOT/%{_includedir}/b64/  include/b64/*

# Only static, so we don't need ldconfig scriptlets

%files tools
%license LICENSE
%doc AUTHORS README
%{_bindir}/libb64-base64

%files devel
%license LICENSE
%{_includedir}/b64
%{_libdir}/libb64.a

%changelog
%autochangelog

%global source0_hash 8a70b6dc85261e6e6e57769bd81ac1e09c0a4c96bbd5e358ffbc2dee51e8e50a
Name:           AMF
Epoch:          1
Version:        1.5.2
Release:        1%{?dist}
Summary:        Advanced Media Framework (AMF) SDK
License:        MIT
URL:            https://gpuopen.com/advanced-media-framework/
BuildArch:      noarch
Source0:        https://github.com/GPUOpen-LibrariesAndSDKs/AMF/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-tarball.sh
# oreon:deps

# /oreon:deps
%description
A light-weight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed source AMD
Pro driver and OpenMax on the open source AMD Mesa driver.

%package        devel
Summary:        Development files for %{name}
%description    devel
A light-weight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed source AMD
Pro driver and OpenMax on the open source AMD Mesa driver.

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        samples
Summary:        Sample files for %{name}
%description    samples
The %{name}-samples package contains sample programs and source for applications
that use %{name}.

%package        docs
Summary:        PDF documentation for %{name}
%description    docs
The %{name}-docs package contains the development documentation in PDF format
that is available in the main %{name}-devel package in Markdown format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
rm -rf Thirdparty

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -fr amf/public/include/* %{buildroot}%{_includedir}/%{name}/
mkdir -p %{buildroot}%{_usrsrc}/%{name}
cp -fr amf/public/* %{buildroot}%{_usrsrc}/%{name}/
rm -fr %{buildroot}%{_usrsrc}/%{name}/include
ln -sf ../../include/AMF %{buildroot}%{_usrsrc}/%{name}/include
mkdir pdf
mv amf/doc/*pdf pdf/
%oreon_autofiles AMF-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles AMF-samples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles AMF-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n AMF-devel -f %{oreon_filedir}/AMF-devel.list
%files -n AMF-samples -f %{oreon_filedir}/AMF-samples.list
%files -n AMF-docs -f %{oreon_filedir}/AMF-docs.list

%changelog

%autochangelog

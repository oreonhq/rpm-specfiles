%global source0_hash bf80ee4a77a731c5a2351b4dd74f524a18806a70099ba66a8058d91aac1150b5

Name:           AMF
Epoch:          1
Version:        1.5.0
Release:        %autorelease
Summary:        Advanced Media Framework (AMF) SDK
License:        MIT
URL:            https://gpuopen.com/advanced-media-framework/
BuildArch:      noarch

Source0:        https://github.com/GPUOpen-LibrariesAndSDKs/AMF/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-tarball.sh

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

# Split out PDF docs
mkdir pdf
mv amf/doc/*pdf pdf/

%files devel
%license LICENSE.txt
%doc amf/doc/*
%{_includedir}/%{name}/

%files samples
%license LICENSE.txt
%{_usrsrc}/%{name}

%files docs
%license LICENSE.txt
%doc pdf/*

%changelog
%autochangelog

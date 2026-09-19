%global source0_hash a22a228064dd530589b98130b9a2b5a6c0e34079b050d462189ab84e70097658

# Run tests in check section
# Requires a usb device
%bcond check 1
%global debug_package %{nil}

# https://github.com/google/gousb
%global goipath         github.com/google/gousb
Version:                1.1.1

%global common_description %{expand:
The gousb package is an attempt at wrapping the libusb library into a 
Go-like binding.}

%gometa

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md

%global godevelheader %{expand:
Requires:       pkgconfig(libusb)}

Name:           %{goname}
Release:        %autorelease
Summary:        Idiomatic Go bindings for libusb-1.0

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  pkgconfig(libusb)

%description
%{common_description}

%gopkg

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog

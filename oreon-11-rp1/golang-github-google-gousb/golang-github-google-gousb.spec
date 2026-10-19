%global source0_hash c78e442e374ea6fa9f169af42f5e41aae7f26b815f0bed144f3ec39506038fff
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/google/gousb
Version:                2.1.0
%global common_description %{expand:
The gousb package is an attempt at wrapping the libusb library into a 
Go-like binding.}
%gometa
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTING.md README.md
%global godevelheader %{expand:
Requires:       pkgconfig(libusb)}
Name:           %{goname}
Release:        1%{?dist}
Summary:        Idiomatic Go bindings for libusb-1.0
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gousb-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(libusb)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

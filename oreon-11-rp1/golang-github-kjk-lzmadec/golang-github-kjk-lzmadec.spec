%global source0_hash 032b4cdc62da77cbbeb57a38636704684e9b68e2d33cbc1bc3c2401bfc54e3c2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/kjk/lzmadec
%global commit          19ac3ee91a71d6a1d7d56f8f72423385d76eb5af
%gometa -f
%global common_description %{expand:
Decompress .7z files in Go using 7z executable.}
%global golicenses      LICENSE
%global godocs          readme.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Decompress .7z files in Go using 7z executable
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/lzmadec-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

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

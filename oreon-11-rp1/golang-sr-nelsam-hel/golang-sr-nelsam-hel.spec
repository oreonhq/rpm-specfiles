%global source0_hash 72dd6cfe94f325a03f3af0503541f919ce67aa789a981e3ca58d4c0321150a0e
%bcond check 0
%global goipath         git.sr.ht/~nelsam/hel
%global forgeurl        https://git.sr.ht/~nelsam/hel
Version:                0.4.6
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Hel is the norse goddess that rules over Helheim, where the souls of those who
did not die in battle go.
This little tool is similar; it generates (hopefully simple) mocks of Go
interface types and stores them in helheim_test.go (by default).}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Mock generator for Go
License:        Unlicense
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{tag}.tar.gz#/hel-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       hel
Summary:        Mock generator for Go
BuildArch:      noarch

%description -n hel
Mock generator for Go

%description %{common_description}

%package -n     hel
Summary:        Mock generator for Go
%description -n hel %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/hel %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles hel usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n hel -f %{oreon_filedir}/hel.list

%changelog

%autochangelog

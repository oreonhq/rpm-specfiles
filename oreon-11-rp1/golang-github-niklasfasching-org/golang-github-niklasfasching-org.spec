%global source0_hash ae161d20bbcc3868383bd2d7c11140fa82caae78a03401d9c15afc94a449822d
%bcond check 0
%global goipath         github.com/niklasfasching/go-org
Version:                1.9.1
%gometa
%global common_description %{expand:
Org mode parser with html & pretty printed org rendering.}
%global golicenses      LICENSE
%global godocs          README.org
Name:           %{goname}
Release:        1%{?dist}
Summary:        Org mode parser with html & pretty printed org rendering
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-org-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       go-org
Summary:        Org mode parser with html & pretty printed org rendering
BuildArch:      noarch

%description -n go-org
Org mode parser with html & pretty printed org rendering

%description
%{common_description}

%package -n go-org
Summary:        Org mode parser with html & pretty printed org rendering
%description -n go-org
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/go-org %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles go-org usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n go-org -f %{oreon_filedir}/go-org.list

%changelog

%autochangelog

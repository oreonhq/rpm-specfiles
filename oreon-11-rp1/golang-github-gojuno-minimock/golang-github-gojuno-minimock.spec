%global source0_hash e368e1df3aa5d84ef5d3cfb61271b30347740a39c0af222db77a39c6d990facb
%global goipath         github.com/gojuno/minimock
Version:                3.4.7
%gometa
%global common_description %{expand:
Powerful mock generation tool for Go programming language.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Powerful mock generation tool for Go programming language
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/minimock-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/davecgh/go-spew/spew)
BuildRequires:  golang(github.com/hexdigest/gowrap/generator)
BuildRequires:  golang(github.com/hexdigest/gowrap/pkg)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/pmezard/go-difflib/difflib)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(golang.org/x/tools/go/packages)
# /oreon:deps
%description
%{common_description}

%package -n     minimock
Summary:        Powerful mock generation tool for Go programming language
%description -n minimock
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles minimock usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n minimock -f %{oreon_filedir}/minimock.list

%changelog

%autochangelog

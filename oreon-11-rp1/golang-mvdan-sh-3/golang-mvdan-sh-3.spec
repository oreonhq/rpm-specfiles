%global source0_hash 89eafc8790df93305dfa42233e262fb25e1c96726a3db420a7555abadf3111ed
%bcond check 0
%global goipath         mvdan.cc/sh/v3
%global forgeurl        https://github.com/mvdan/sh
Version:                3.7.0
%gometa
%global common_description %{expand:
A shell parser, formatter, and interpreter. Supports POSIX Shell, Bash, and
mksh.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A shell parser, formatter, and interpreter
License:        BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/sh-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/creack/pty)
BuildRequires:  golang(github.com/frankban/quicktest)
BuildRequires:  golang(github.com/kr/pretty)
BuildRequires:  golang(github.com/rogpeppe/go-internal/testscript)
BuildRequires:  scdoc
# /oreon:deps
%description
%{common_description}

%package -n     shfmt
Summary:        Shell formatter
%description -n shfmt
shfmt is a shell formatter. shfmt's default shell formatting was chosen to be
consistent, common, and predictable.

%package -n     gosh
Summary:        Proof of concept shell that uses interp
%description -n gosh
Proof of concept shell that uses interp. Note that it's not meant to replace a
POSIX shell at the moment, and its options are intentionally minimalistic.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
mkdir -p %{gobuilddir}/man
scdoc < cmd/shfmt/shfmt.1.scd > %{gobuilddir}/man/shfmt.1
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1/
install -m 0644 -vp %{gobuilddir}/man/* %{buildroot}%{_mandir}/man1/
%oreon_autofiles shfmt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gosh usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck -t cmd
%endif
%files -f %{oreon_filedir}/main.list
%files -n shfmt -f %{oreon_filedir}/shfmt.list
%files -n gosh -f %{oreon_filedir}/gosh.list

%changelog

%autochangelog

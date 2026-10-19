%global source0_hash bd79aa6515af4e82a86aa6984b7fc02697d35cb7a4764e1e51eb528cf8f57c31
%bcond check 0
%global goipath         github.com/zmap/zlint/v3
%global forgeurl        https://github.com/zmap/zlint
Version:                3.5.0
%gometa
%global common_description %{expand:
ZLint is a X.509 certificate linter written in Go that checks for consistency
with standards (e.g. RFC 5280) and other relevant PKI requirements (e.g.
CA/Browser Forum Baseline Requirements).}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        X.509 Certificate Linter focused on Web PKI standards and requirements
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/zlint-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  help2man
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1
mv v3/* ./.

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr --no-info --version-string=%{version} %{buildroot}%{_bindir}/zlint > %{buildroot}%{_mandir}/man1/zlint.1
help2man --no-discard-stderr --no-info --version-string=%{version} %{buildroot}%{_bindir}/zlint-gtld-update > %{buildroot}%{_mandir}/man1/zlint-gtld-update.1
%oreon_autofiles main
%if %{with check}
%check

%gocheck -t cmd
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

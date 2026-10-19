%global source0_hash 58969a6975e14a2d69228d7330f656f9d6dac8d47c1ad3ffd09ddf3ea12f6171
%bcond check 0
%global goipath         github.com/zmap/zcertificate
Version:                0.0.1
%gometa
%global common_description %{expand:
ZCertificate parses X.509 certificates and runs ZLint.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Command line utility for parsing certificates
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/zcertificate-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/sirupsen/logrus)
BuildRequires:  golang(github.com/zmap/zcrypto/data/test/certificates)
BuildRequires:  golang(github.com/zmap/zcrypto/x509)
BuildRequires:  golang(github.com/zmap/zlint/v3)
BuildRequires:  help2man
# /oreon:deps
%description
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
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
pushd %{buildroot}%{_bindir}
help2man --no-discard-stderr --no-info --version-string=1 ./zcertificate --output=%{buildroot}%{_mandir}/man1/zcertificate.1
popd
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

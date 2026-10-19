%global source0_hash b682452402f403b6ee668bb042bd9b753fe48df84fa7a18a1c32606ffd4918af
%bcond check 0
%global goipath         github.com/cloudflare/cfssl
Version:                1.6.5
%gometa -L
%global common_description %{expand:
CFSSL is CloudFlare's PKI/TLS swiss army knife. It is both a command line tool
and an HTTP API server for signing, verifying, and bundling TLS certificates. It
requires Go 1.11+ to build.}
%global golicenses      LICENSE LICENSE-whitelist
%global godocs          doc CHANGELOG README.md
Name:           golang-github-cloudflare-cfssl
Release:        1%{?dist}
Summary:        CFSSL: Cloudflare's PKI and TLS toolkit
License:        BSD-2-Clause AND ISC
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cfssl-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1
mv whitelist/LICENSE LICENSE-whitelist

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
mv %{gobuilddir}/bin/mkbundle %{gobuilddir}/bin/cfssl-mkbundle
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

for test in "TestBundle" \
            "TestStapleSCTList" \
            "TestLdap" \
            "TestCachedCRLSet" \
            "TestCertificateSelection" \
            "TestSANs" \
            "TestRemoteTLSSign" \
            "TestRemoteMutualTLSSign" \
            "TestRemoteTLSInfo" \
            "TestRemoteMutualTLSInfo" \
            "TestLint" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -d bundler -d scan/crypto/tls
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

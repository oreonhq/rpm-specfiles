%global source0_hash 4c73b6badcb6337cb3ec895b4d0a819c2b6e7d6b1b6e753549d4ee6f2c2df29f
%bcond check 0
%global goipath         github.com/nats-io/nkeys
Version:                0.4.16
%gometa
%global common_description %{expand:
A public-key signature system based on Ed25519 for the NATS ecosystem.}
%global golicenses      LICENSE
%global godocs          GOVERNANCE.md MAINTAINERS.md README.md TODO.md\\\
                        README-nk.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Public-key signature system based on Ed25519 for the NATS ecosystem
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/nkeys-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/crypto/ed25519)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
mv nk/README.md README-nk.md

%build

for cmd in nk; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

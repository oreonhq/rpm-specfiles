%global source0_hash 4e5914f1ee3e5f384d605406f30799bf556a06b9785d5b0e555fd88b43daf19c
%bcond check 1
%global goipath         github.com/checkmake/checkmake
Version:                0.2.2
%global tag             0.2.2
%global commit          723c897a3cc9693f1db8ede3714ed63f926d280f
%gometa -L -f
Name:           checkmake
Release:        1%{?dist}
Summary:        Linter/analyzer for Makefiles
License:        Apache-2.0 AND BSD-3-Clause AND ISC AND MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  pandoc
# /oreon:deps
%description
Linter/analyzer for Makefiles.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}

%build

%global gomodulesmode GO111MODULE=on
export GO_LDFLAGS="-X \"main.version=%{version}\" \
                   -X \"main.buildTime=$(date -u -d@$SOURCE_DATE_EPOCH +"%Y-%m-%dT%H:%M:%SZ")\" \
                   -X \"main.builder=Fedora\" \
                   -X \"main.goversion=$(go version)\""
%gobuild -o %{gobuilddir}/bin/checkmake ./cmd/checkmake
sed "s/REPLACE_DATE/$(date -u -d@$SOURCE_DATE_EPOCH +"%Y-%m-%dT%H:%M:%SZ")/" man/man1/checkmake.1.md | pandoc -s -t man -o checkmake.1
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp _build/bin/checkmake %{buildroot}%{_bindir}/
install -m 0755 -vd %{buildroot}%{_mandir}/man1/
install -m 0644 -vp checkmake.1 %{buildroot}%{_mandir}/man1/checkmake.1
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
%gotest ./...
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

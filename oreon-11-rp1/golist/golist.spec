%global source0_hash 058705d7264a288d64ea8e1be2c5b877ba70199a58424d6a5dbdc2c493e8641d
%global source1_hash 4846e57043af0989a3ac66589d5c4a9b3b9e1aadbcc0ee41719038850b6fd5d0

%bcond check 1

Name:           golist
Version:        0.11.0
Release:        %autorelease
Summary:        A tool to analyse the properties of a Go (Golang) codebase
License:        BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://forge.fedoraproject.org/go/golist
Source0:        %{url}/archive/v%{version}.tar.gz#/golist-%{version}.tar.gz
Source1:        golist-%{version}-vendor.tar.bz2
Source2:        go-vendor-tools.toml

ExclusiveArch:  %{golang_arches}
BuildRequires:  go-vendor-tools
BuildRequires:  go-rpm-macros

%description
A tool to analyse the properties of a Go (Golang) codebase.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -n golist -p1
tar -xf %{SOURCE1}

%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:2}

%build
%global gomodulesmode GO111MODULE=on
%gobuild -o golist ./cmd/golist

%install
%go_vendor_license_install -c %{S:2}
install -Dp ./golist -t %{buildroot}%{_bindir}

%check
%go_vendor_license_check -c %{S:2}
%if %{with check}
%gocheck2
%endif

%files -f %{go_vendor_license_filelist}
%doc NEWS.md README.md
%{_bindir}/golist

%changelog
%autochangelog

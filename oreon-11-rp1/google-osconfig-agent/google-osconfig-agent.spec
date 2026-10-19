%global source0_hash f8dbcf878bc10d9752cb30a8403bc4f4618c368fe214a6a5157e4c161cf014ed
%bcond check 0
%bcond vendor 1
%global goipath         github.com/GoogleCloudPlatform/osconfig
Version:                20241029.01
%global tag             %{version}
%gometa -f
%global common_description %{expand:
Google OS Config Agent}
Name:           google-osconfig-agent
Release:        1%{?dist}
Summary:        Google OS Config Agent
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/osconfig-%{version}.tar.gz
Source1:        osconfig-%{version}-vendor.tar.gz
Source2:        LICENSES.dependencies
ExcludeArch:    ppc64le s390x
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 %{forgesetupargs} %{?with_vendor:-b1}
%goprep -e %{?with_vendor:-k}
cp %{SOURCE2} .

# Examples directory isn't needed.
rm -rf examples

# e2e_tests require connectivity to Google's APIs and extra packages.
rm -rf e2e_tests

%build

%gobuild -o %{gobuilddir}/bin/google_osconfig_agent %{goipath}
%install
install -m0755 -vd                      %{buildroot}%{_bindir}
install -m0755 -vp %{gobuilddir}/bin/*  %{buildroot}%{_bindir}/
install -m0644 -Dp %{name}.service      %{buildroot}%{_unitdir}/%{name}.service
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d config -d policies
%endif
%post

%systemd_post %{name}
%preun

%systemd_preun %{name}
%postun

%systemd_postun_with_restart %{name}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

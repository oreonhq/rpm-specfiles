%global source0_hash 203b1aa2e3aa09af415a96a0afc98eef4acf845ab8af57bf9f7569bd13161717
%bcond_without tests
%bcond_with    all_tests
Name:           dnsviz
Version:        0.11.1
Release:        1%{?dist}
Summary:        Tools for analyzing and visualizing DNS and DNSSEC behavior
License:        GPL-2.0-or-later
URL:            https://github.com/dnsviz/dnsviz
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch1:         dnsviz-0.11-no-sha1.patch
BuildArch:      noarch
Requires:       python3-pygraphviz >= 1.3
Requires:       python3-dns >= 1.13
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dnsviz = %{version}-%{release}
# /oreon:deps
%description
DNSViz is a tool suite for analysis and visualization of Domain Name System
(DNS) behavior, including its security extensions (DNSSEC).  This tool suite
powers the Web-based analysis available at http://dnsviz.net/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%if %{with tests}
export DNSVIZ_SHARE_PATH="%{buildroot}%{_datadir}%{name}"
%if %{with all_tests}
  if ! [ -f /etc/resolv.conf ]; then
    echo "nameserver 127.0.0.1" | tee /etc/resolv.conf
    OWN_RESOLV=y
  fi
  %pytest
  if [ "$OWN_RESOLV" = y ]; then
    rm -f /etc/resolv.conf
  fi
%else
  %pytest -k "not probe_options and not probe_run_online and not test_dnsviz_graph_output_format and not _online"
%endif
%endif
%files

%changelog

%autochangelog

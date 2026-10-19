%global source0_hash 05e2478bea87cf41bd9cc49ee6a074c116458950ba07f9173b42f1cbc3400b1e
Name:           hstsparser
Version:        1.2.0
Release:        1%{?dist}
Summary:        HSTS Digital Forensics parser
License:        MIT
URL:            https://github.com/thebeanogamer/hstsparser
Source0:        https://github.com/thebeanogamer/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
%py_provides python3-hstsparser
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.3
Requires:       python3-hstsparser = %{version}-%{release}
# /oreon:deps
%description
Parse Firefox and Chrome HSTS databases into Digital Forensics artifacts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir hstsparser-%{version}
%oreon_prep
%build

%pyproject_wheel
ln -s hstsparser.py hstsparser
help2man -N ./hstsparser -o hstsparser.1 --version-string='%{version}'
rm -f hstsparser
%install
%pyproject_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -pm 0644 hstsparser.1 %{buildroot}%{_mandir}/man1/hstsparser.1
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

%autochangelog

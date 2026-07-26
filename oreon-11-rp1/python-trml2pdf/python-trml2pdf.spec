%global source0_hash e6069f4724b306867d59f1419e936a57bd62c6a7993c83f3b6645c46059d01f0

%global	module	trml2pdf

Name:		python-%{module}
Version:	0.6
Release:	21%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2
Summary:	Easy creating PDF using ReportLab's RML
URL:		https://github.com/romanlv/trml2pdf
Source0:	https://github.com/romanlv/trml2pdf/archive/%{version}/%{module}-%{version}.tar.gz
BuildRequires:	python3-setuptools
# python3-devel
BuildRequires:	pkgconfig(python3)
# python3-pytest
BuildRequires:	%{py3_dist pytest}
# python3-six
BuildRequires:	%{py3_dist six} >= 1.9
# python3-reportlab
BuildRequires:	%{py3_dist reportlab} >= 3.2
Requires:	%{py3_dist reportlab} >= 3.2
BuildArch:	noarch

%description
Open source implementation of RML (Report Markup Language) from ReportLab

%package -n	python3-%{module}
Summary:	%{summary}
%py_provides python3-%{module}

%description -n	python3-%{module}
Open source implementation of RML (Report Markup Language) from ReportLab

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{module}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{module}
%{__install} -Dp -m0644 doc/trml2pdf.1 %{buildroot}%{_mandir}/man1/trml2pdf.1

%check
%{pytest}

%files -n python3-%{module} -f %{pyproject_files}
%license LICENSE.txt doc/COPYRIGHT.txt
%doc README.md doc/CREDITS.md
%{_bindir}/%{module}
%{_mandir}/man1/trml2pdf.1.*

%changelog
%autochangelog

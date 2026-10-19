%global source0_hash 857e8741014ec5015f7a00aafb5dccbb56378ef4c1da55a828d44bcf5ff3acdb
Name: rst2pdf
Version: 0.105
Release:        1%{?dist}
Summary:        Tool for transforming reStructuredText to PDF
License: MIT
URL: https://rst2pdf.org/
Source0:        https://files.pythonhosted.org/packages/source/r/rst2pdf/rst2pdf-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-rst2pdf = %{version}-%{release}
# /oreon:deps
%package -n       python3-rst2pdf+aafiguresupport
Summary:        Metapackage for python3-rst2pdf aafiguresupport extras
Requires:       python3-rst2pdf = %{version}-%{release}
Provides:       python3dist(rst2pdf[aafiguresupport]) = %{version}-%{release}

%description -n python3-rst2pdf+aafiguresupport
Metapackage for python3-rst2pdf aafiguresupport extras.

%package -n       python3-rst2pdf+mathsupport
Summary:        Metapackage for python3-rst2pdf mathsupport extras
Requires:       python3-rst2pdf = %{version}-%{release}
Provides:       python3dist(rst2pdf[mathsupport]) = %{version}-%{release}

%description -n python3-rst2pdf+mathsupport
Metapackage for python3-rst2pdf mathsupport extras.

%package -n       python3-rst2pdf+plantumlsupport
Summary:        Metapackage for python3-rst2pdf plantumlsupport extras
Requires:       python3-rst2pdf = %{version}-%{release}
Provides:       python3dist(rst2pdf[plantumlsupport]) = %{version}-%{release}

%description -n python3-rst2pdf+plantumlsupport
Metapackage for python3-rst2pdf plantumlsupport extras.

%package -n       python3-rst2pdf+rawhtmlsupport
Summary:        Metapackage for python3-rst2pdf rawhtmlsupport extras
Requires:       python3-rst2pdf = %{version}-%{release}
Provides:       python3dist(rst2pdf[rawhtmlsupport]) = %{version}-%{release}

%description -n python3-rst2pdf+rawhtmlsupport
Metapackage for python3-rst2pdf rawhtmlsupport extras.

%package -n       python3-rst2pdf+sphinx
Summary:        Metapackage for python3-rst2pdf sphinx extras
Requires:       python3-rst2pdf = %{version}-%{release}
Requires:       python3dist(sphinx) > 7.3
Requires:       python3dist(sphinx) >= 8.2
Provides:       python3dist(rst2pdf[sphinx]) = %{version}-%{release}

%description -n python3-rst2pdf+sphinx
Metapackage for python3-rst2pdf sphinx extras.

%package -n       python3-rst2pdf+svgsupport
Summary:        Metapackage for python3-rst2pdf svgsupport extras
Requires:       python3-rst2pdf = %{version}-%{release}
Provides:       python3dist(rst2pdf[svgsupport]) = %{version}-%{release}

%description -n python3-rst2pdf+svgsupport
Metapackage for python3-rst2pdf svgsupport extras.

%description
Tool for transforming reStructuredText to PDF using ReportLab

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p 1
# Remove version limit for packaging and docutils
sed -i 's/"packaging.*"/"packaging"/' pyproject.toml
sed -i 's/"docutils.*"/"docutils"/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%doc CHANGES.rst Contributors.txt README.rst
%license LICENSE.txt
%{_bindir}/%{name}
%oreon_autofiles main

%files

%changelog

%autochangelog

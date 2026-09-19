%global source0_hash 948a645f8f0bc3abe7fd587019a2197a12436cd73d0d4908af95bfc8da337588

%global upname html2text
%global common_sum Convert HTML to Markdown-formatted text
%global common_desc %{upname} is a Python script that converts a page \
of HTML into clean, easy-to-read plain ASCII text.  Better yet, that ASCII \
also happens to be valid Markdown (a text-to-HTML format).

Name:           python-%{upname}
Version:        2025.4.15
Release:        6%{?dist}
Summary:        %{common_sum}

License:        GPL-3.0-or-later
URL:            https://github.com/Alir3z4/%{upname}/
Source0:        https://files.pythonhosted.org/packages/source/h/%{upname}/%{upname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python3-pytest

%description
%{common_desc}

%package -n python3-%{upname}
Summary:        %{common_sum}
Provides:       %{upname} = %{version}-%{release}
Obsoletes:      python2-%{upname} <= %{version}-%{release}
%{?python_provide:%python_provide python3-%{upname}}

%description -n python3-%{upname}
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files html2text

%{__mkdir} -p %{buildroot}%{_mandir}/man1

%{__mv} -f %{buildroot}%{_bindir}/%{upname} %{buildroot}%{_bindir}/python3-%{upname}
export PYTHONPATH="%{buildroot}%{python3_sitelib}"
help2man --no-discard-stderr -s 1 -N -o %{buildroot}%{_mandir}/man1/python3-%{upname}.1 %{buildroot}%{_bindir}/python3-%{upname}
pushd  %{buildroot}%{_bindir}
ln -s python3-%{upname} %{upname}
ln -s python3-%{upname} %{name}
popd
pushd %{buildroot}%{_mandir}/man1/
ln -s python3-%{upname}.1 %{upname}.1
ln -s python3-%{upname}.1 %{name}.1
popd

%check
%pyproject_check_import
%{__python3} -m pytest
%pytest %{_builddir}

%files -n python3-%{upname} -f %{pyproject_files}
%license AUTHORS.* COPYING
%doc README.* ChangeLog.* PKG-INFO
%{_bindir}/python3-%{upname}
%{_bindir}/%{upname}
%{_bindir}/%{name}
%{_mandir}/man1/python3-%{upname}.1*
%{_mandir}/man1/%{upname}.1*
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog

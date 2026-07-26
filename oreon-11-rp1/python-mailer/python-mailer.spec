%global source0_hash 3411a12197731e0d5379ab194d9acc8d0d71c8b95fdfb11474d67c3e9860070e

%global srcname mailer

Name:           python-%{srcname}
Version:        0.8.1
Release:        34%{?dist}
Summary:        A module that simplifies sending email

License:        MIT
URL:            http://pypi.python.org/pypi/mailer
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.zip

Patch0:		dont-use-2to3.patch

BuildArch:      noarch

%description
Simple front end to the smtplib and email modules, to simplify sending email.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:	python3-devel
BuildRequires:	pyproject-rpm-macros
%py_provides python3-%{srcname}

%description -n python3-%{srcname}
Simple front end to the smtplib and email modules, to simplify sending email.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mailer

%files -n python3-%{srcname} -f %{pyproject_files}

%changelog
%autochangelog

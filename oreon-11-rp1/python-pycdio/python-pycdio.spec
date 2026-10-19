%global source0_hash 61734db8c554b7b1a2cb2da2e2c15d3f9f5973a57cfb06f8854c38029004a9f8
Name:		python-pycdio
Version:	2.1.1
Release:        1%{?dist}
Summary:        A Python interface to the CD Input and Control library
License:	GPL-3.0-or-later
URL:		http://www.gnu.org/software/libcdio/
Source0:        https://files.pythonhosted.org/packages/source/p/pycdio/pycdio-2.1.1.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pycdio = %{version}-%{release}
# /oreon:deps
%description
The pycdio (and libcdio) libraries encapsulate CD-ROM reading and
control. Python programs wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

%package -n python3-pycdio
Summary:	A Python interface to the CD Input and Control library
Obsoletes:	pycdio < 2.0.0-6
Provides:	pycdio = %{version}-%{release}
%{?python_provide:%python_provide python3-pycdio}
%description -n python3-pycdio
The pycdio (and libcdio) libraries encapsulate CD-ROM reading and
control. Python programs wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n pycdio-%{version} -p1
# hotfix for Python 3.12, please bring this upstream
# fixes https://bugzilla.redhat.com/2155240
sed -i 's/assertEquals/assertEqual/' test/test-cdtext.py

%build

%pyproject_wheel
%install
%pyproject_install
chmod 755 %{buildroot}/%{python3_sitearch}/*.so
%oreon_autofiles python3-pycdio usr/lib/python3*/site-packages/pycdio* usr/lib64/python3*/site-packages/pycdio* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pycdio* usr/lib64/python3*/site-packages/pycdio* usr/bin/*

%files
%files -n python3-pycdio -f %{oreon_filedir}/python3-pycdio.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-10
- Prepare for Oreon 11 (RP1)

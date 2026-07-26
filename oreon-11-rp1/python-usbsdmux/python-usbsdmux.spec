%global source0_hash a04747b1fce007458b7ec15ffec5298e442a21aac50ff6e89fbd7a1f7bb60f2a

%global srcname usbsdmux

Name:           python-usbsdmux
Version:        25.08
Release:        %autorelease
Summary:        USB-SD-Mux control software and library
License:        LGPL-2.1-or-later
URL:            https://github.com/linux-automation/usbsdmux/
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Source1:        99-usbsdmux.rules

BuildArch:      noarch

BuildRequires:  help2man
Buildrequires:  python3-pytest
Buildrequires:  python3-pytest-mock
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sed

%{?python_enable_dependency_generator}

%global _description %{expand:
usbsdmux is used to control a special piece of hardware called the USB-SD-Mux.
It can be used via the command line or as a Python library
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       systemd-udev

Provides:       %{srcname} = %{version}-%{release}

Recommends:     python3-paho-mqtt

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Remove the python shebang from non-executable files.
sed -i '1{\@^#!.*/usr/bin/env python@d}' usbsdmux/*.py

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
install -p -m 644 -D %{SOURCE1} %{buildroot}%{_udevrulesdir}/99-usbsdmux.rules
mkdir -p %{buildroot}%{_mandir}/man1
for BBIN in usbsdmux usbsdmux-configure ; do
    help2man --no-discard-stderr %{buildroot}%{_bindir}/$BBIN > %{buildroot}%{_mandir}/man1/$BBIN.1
done

%pyproject_save_files -l usbsdmux

%check
%pyproject_check_import
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSES/LGPL-2.1-or-later.txt
%doc AUTHORS README.rst contrib
%{_bindir}/usbsdmux*
%{_mandir}/man1/usbsdmux*1*
%{_udevrulesdir}/99-usbsdmux.rules

%changelog
%autochangelog

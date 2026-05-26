# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 e11c37bec51e9e0a9422b41ee2db36728e1ee699aa202ae94bc2e77f7fa6b99e
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           python-evdev
Version:        1.9.3
Release:        %autorelease
Summary:        Python bindings for the Linux input handling subsystem

License:        BSD-3-Clause
URL:            https://python-evdev.readthedocs.io
Source0:        https://github.com/gvalkov/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  kernel-headers


%global _description \
This package provides python bindings to the generic input event interface in \
Linux. The evdev interface serves the purpose of passing events generated in \
the kernel directly to userspace through character devices that are typically \
located in /dev/input/. \
 \
This package also comes with bindings to uinput, the userspace input subsystem. \
Uinput allows userspace programs to create and handle input devices that can \
inject events directly into the input subsystem. \
 \
In other words, python-evdev allows you to read and write input events on Linux. \
An event can be a key or button press, a mouse movement or a tap on a \
touchscreen.


%description %{_description}


%package -n python3-evdev
Summary:        %{summary}
%{?python_provide:%python_provide python3-evdev}
%description -n python3-evdev %{_description}


#------------------------------------------------------------------------------
%prep
%oreon_verify_sources
%autosetup

%generate_buildrequires
%pyproject_buildrequires

#------------------------------------------------------------------------------
%build
%pyproject_wheel

#------------------------------------------------------------------------------
%install
%pyproject_install
%pyproject_save_files evdev

%check
%pyproject_check_import -t


#------------------------------------------------------------------------------
%files -n python3-evdev -f %{pyproject_files}
%license LICENSE
%doc README.md

#------------------------------------------------------------------------------
%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.3-1
- Prepare for Oreon 11 (RP1)

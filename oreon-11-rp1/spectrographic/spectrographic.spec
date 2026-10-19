%global source0_hash 374f1eaeead348ee73147e7ba3ebf4ded8925c66dab2861b1f6572ab81a5a613
%global pypi_name spectrographic
Name: %{pypi_name}
Summary:        Turn an image into sound whose spectrogram looks like the image
License: MIT
Version: 0.9.3
Release:        23%{?dist}
URL: https://github.com/LeviBorodenko/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/source/s/spectrographic/spectrographic-%{version}.tar.gz
Patch0: 0000-remove-pyscaffold-max-version-constraint.patch
Patch1: 0001-add-version-metadata.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pillow
BuildRequires:  python3-pyscaffold
BuildRequires:  python3-setuptools
BuildRequires:  python3-simpleaudio
BuildRequires:  python3-sphinx
BuildRequires:  python3-wavio
# /oreon:deps
%description
Turn any image into a sound whose spectrogram looks like the image!

Most sounds are intricate combinations of many acoustic waves, each having
different frequencies and intensities. A spectrogram is a way to represent
sound by plotting time on the horizontal axis and the frequency spectrum
on the vertical axis. Sort of like sheet music on steroids.

What this tool does is, taking an image and simply interpreting it
as a spectrogram. Therefore, by generating the corresponding sound,
we have embedded our image in a spectrogram.

%package doc
Summary: Documentation for %{pypi_name}
BuildArch: noarch
%description doc
This package contains documentation (in HTML format)
for the %{pypi_name} program.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -e 's/\b__RPM_PACKAGE_VERSION__\b/%{version}/g' -i setup.cfg

%build

%py3_build
cd docs/
make man
make html
%install
%py3_install
install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 build/sphinx/man/%{name}.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n spectrographic-doc -f %{oreon_filedir}/spectrographic-doc.list

%changelog

%autochangelog

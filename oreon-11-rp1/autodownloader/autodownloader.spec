%global source0_hash 65f8ab27c015139fa109592a668ea0ffc2fd322634c70871660e0e05ef58aa2f

Name:           autodownloader
Version:        0.5.0
Release:        16%{?dist}
Summary:        GUI-tool to automate the download of certain files
License:        GPL-2.0-or-later
URL:            https://github.com/frenzymadness/AutoDownloader
Source0:        https://github.com/frenzymadness/AutoDownloader/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires: make
Requires:       python3-gobject python3-six gtk3 hicolor-icon-theme

%description
Some software (usually games) requires certain data files to operate, sometimes
these datafiles can be freely downloaded but may not be redistributed and thus
cannot be put into so called packages as part of a distro.

autodownloader is a tool which can be used as part of a package to automate the
download of the needed files. It will prompt the user explaining to him the
need of the download and asking if it is ok to make an internet connection,
after this it will show the license of the to be downloaded files and last it
will do the actual download and md5 verification off these files. This whole
process can be configured by the packager through a simple configuration file.

Notice that Autodownloader while open source itself, may download files which
are not permitted to be (re)distributed unlike most files in Fedora.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AutoDownloader-%{version}
%py3_shebang_fix .

# Avoid hardcoding /usr prefix
sed -i -e 's!/usr/bin!%{_bindir}!' Makefile
sed -i -e 's!/usr/share!%{_datadir}!' Makefile

%build
# nothing to build pure python code only

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%license COPYING
%doc ChangeLog README.txt examples/example.autodlrc
%{_bindir}/autodl
%{_datadir}/autodl
%{_datadir}/icons/hicolor/*/apps/autodl.png

%changelog
%autochangelog

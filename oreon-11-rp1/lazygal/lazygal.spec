%global source0_hash 29944ae262c75f69a52bca331e2223173e2ba06774ea2e477c4f01b5cc04ad06
Name:           lazygal
Version:        0.12
Release:        1%{?dist}
Summary:        A static web gallery generator
License:        GPL-2.0-or-later AND MIT
URL:            https://sml.zincube.net/~niol/repositories.git/lazygal/about/
Source0:        https://sml.zincube.net/~niol/repositories.git/lazygal/snapshot/lazygal-%{version}.tar.bz2
BuildArch:      noarch
Recommends:     /usr/bin/ffmpeg
Recommends:     /usr/bin/ffprobe
Requires:       js-jquery
Requires:       python3-gexiv2
Requires:       python3dist(genshi)
Requires:       python3dist(pillow)
Provides:       bundled(jquery.tipTip.js) = 1.3
Provides:       bundled(respond.js) = 1.4.2
Provides:       bundled(jquery.colorbox.js) = 1.4.36
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-lazygal = %{version}-%{release}
# /oreon:deps
%description
Lazygal is another static web gallery generator written in Python.
It can be summed up by the following features :
* Command line based (thus scriptable).
* Handles album updates.
* Presents all your pictures and videos and associated data.
* Makes browsing sharing pictures easy.
* Make customization easy.
* Does not change your original pictures directories (the source argument).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%{__python3} setup.py build_i18n
%{__python3} setup.py build_manpages
%install
%pyproject_install
install -dm755 %{buildroot}%{_mandir}/man{1,5}
install -pm644 man/lazygal.1 %{buildroot}%{_mandir}/man1/
install -pm644 man/lazygal.conf.5 %{buildroot}%{_mandir}/man5/
install -dm755 %{buildroot}%{_datadir}/locale
cp -pr build/mo/* %{buildroot}%{_datadir}/locale/
%find_lang %{name}
%oreon_autofiles main

%check

%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest
%files

%changelog

%autochangelog

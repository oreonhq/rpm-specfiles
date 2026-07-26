%global source0_hash 9746b52c62dfd3dc99993d17e82a446d1b43691ae78d450666c9ac2e3e90eafc

# Pull from GitHub, since it has fixes not released on PyPI and contains
# the LICENSE file as well as an additional doc.
%global forgeurl https://github.com/JuanPotato/Legofy
%global commit 0cadceb9f412636c11eb62370682a43ae329e4cb

Name:           legofy
Version:        1.0.0
Release:        %autorelease
Summary:        Make images look as if they are made out of 1x1 LEGO blocks
%forgemeta
# SPDX identifier
License:        MIT
URL:            %forgeurl
Source0:        %forgesource
Source1:        %{name}.1

BuildArch:      noarch
BuildRequires:  python3-devel

%description
Legofy is a python program that takes a static image or gif and makes
it so that it looks as if it was built out of LEGO.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{name}
install -pDm644 %{SOURCE1} %{buildroot}%{_mandir}/man1/legofy.1

%files -f %{pyproject_files}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%doc README.md 2010-LEGO-color-palette.pdf

%changelog
%autochangelog

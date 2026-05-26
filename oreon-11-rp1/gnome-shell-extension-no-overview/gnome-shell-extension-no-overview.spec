%global extension   no-overview
%global uuid        %{extension}@fthx

Name:           gnome-shell-extension-%{extension}
Version:        49
Release:        %autorelease
Summary:        GNOME Shell extension for no overview at start-up
License:        GPL-3.0-only
URL:            https://extensions.gnome.org/extension/4099/no-overview/
Source0:        https://github.com/fthx/no-overview/archive/refs/tags/v%{version}.zip#/no-overview-%{version}.zip

Source1:        https://raw.githubusercontent.com/fthx/no-overview/main/LICENSE#/%{extension}-LICENSE
Source2:        https://raw.githubusercontent.com/fthx/no-overview/main/README.md#/%{extension}-README.md
#Patch0:         %%{name}-HEAD.patch
Patch0:         %{name}-HEAD.patch
# oreon url source checksums begin
%global source0_sha256 69f48fd490c4fd21a0077657ea5462a8b7c41acaa75fc897b91cbed5bb855a00
%global source0_file v49.zip
# oreon url source checksums end
BuildArch:      noarch
# rhbz#2001561 Delete to require gnome-shell-extension-common
#Requires:       gnome-shell-extension-common
Recommends:     gnome-extensions-app
BuildRequires:  git


%description
GNOME Shell extension for no overview at start-up. For GNOME Shell 40+.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v49.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "69f48fd490c4fd21a0077657ea5462a8b7c41acaa75fc897b91cbed5bb855a00" || { echo "oreon: Source0 SHA256 mismatch for v49.zip" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{extension}-%{version} -S git

%build
# Nothing to build here

%install
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

# install main extension files
cp -rp *.js metadata.json \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%files
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 49-1
- Prepare for Oreon 11 (RP1)

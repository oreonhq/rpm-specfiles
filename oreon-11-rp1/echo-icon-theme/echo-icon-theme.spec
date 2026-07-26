%global source0_hash bc757dbfabfd687ae3465a9c420f815ce97cd837185c4dee45eb88b09a49d8ce

%define git_head cc6da5b
%define checkout 20081003
%define alphatag %{checkout}git%{git_head}

Name:           echo-icon-theme
Version:        0.3.89.0
Release:        0.45.%{alphatag}%{?dist}
Summary:        Echo icon theme

# Automatically converted from old format: CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-CC-BY-SA
URL:            http://fedoraproject.org/wiki/Artwork/EchoDevelopment
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  icon-naming-utils >= 0.8.7
BuildRequires: make
#BuildRequires:  autoconf automake
Requires(post): gtk2 >= 2.6.0
# The following replacements for gnome-themes don't cover everything.
# Most of Mist (the fallback for echo) was provided by gnome-themes.
# Eventually that should get fixed or echo should be retired.
Requires:       gnome-icon-theme
Requires:       gtk2-engines

%description
This package contains the Echo icon theme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

touch %{buildroot}%{_datadir}/icons/Echo/icon-theme.cache

%post
touch --no-create %{_datadir}/icons/Echo || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/Echo || :

%files
%doc COPYING ChangeLog AUTHORS
%{_datadir}/icons/Echo
%ghost %{_datadir}/icons/Echo/icon-theme.cache

%changelog
%autochangelog

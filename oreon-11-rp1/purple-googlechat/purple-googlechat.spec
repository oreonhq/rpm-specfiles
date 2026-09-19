%global source0_hash a3c232fc56774798eed065a447d58f808254bb2b8744ba5b33ce3527d601b1de

%global plugin_name googlechat

%global commit0 35a075f7170a5cd276bbbac06175f0b3817a5245
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20251204

Name: purple-%{plugin_name}
Version: 0
Release: 9.%{date}git%{shortcommit0}%{?dist}

License: GPL-3.0-or-later
Summary: Google Chat plugin for libpurple
URL: https://github.com/EionRobb/%{name}
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libprotobuf-c)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(zlib)

BuildRequires: gcc
BuildRequires: make

Provides: purple-hangouts = 1:%{version}-%{release}
Obsoletes: purple-hangouts < 1:0-80.20210629git55b9f01

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Google Chat protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin
Provides: pidgin-hangouts = 1:%{version}-%{release}
Obsoletes: pidgin-hangouts < 1:0-80.20210629git55b9f01

%description
Adds support for Google Chat to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Google Chat protocol implemented by
purple-googlechat.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit0}

# fix W: wrong-file-end-of-line-encoding
sed -i -e "s,\r,," README.md

%build
%set_build_flags
%make_build

%install
%make_install
chmod 755 %{buildroot}%{_libdir}/purple-2/lib%{plugin_name}.so

%files
%{_libdir}/purple-2/lib%{plugin_name}.so
%license LICENSE
%doc README.md

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
%autochangelog

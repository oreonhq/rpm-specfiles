%global source0_hash 38b0b3308d26170eb567763ff5a11012a939ea75a1368415425f18a1f46cac8a
Name:       buku
Version:    5.1.1
Release:        1%{?dist}
Summary:        Powerful command-line bookmark manager
License:    GPL-3.0-or-later
URL:        https://github.com/jarun/Buku
Source0:        https://github.com/jarun/Buku/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:      buku-fix-makefile.patch
BuildArch:  noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.3
Requires:       python3-buku = %{version}-%{release}
# /oreon:deps
%package -n       python3-buku+server
Summary:        Metapackage for python3-buku server extras
Requires:       python3-buku = %{version}-%{release}
Requires:       python3dist(arrow) >= 1.2.2
Requires:       python3dist(flask-admin) >= 2.0.0
Requires:       python3dist(flask-paginate) >= 2022.1.8
Requires:       python3dist(flask-wtf) >= 1.0.1
Requires:       python3dist(flask) >= 2.2.2
Requires:       python3dist(jinja2) >= 3
Provides:       python3dist(buku[server]) = %{version}-%{release}

%description -n python3-buku+server
Metapackage for python3-buku server extras.

%package -n       python3-buku+locales
Summary:        Metapackage for python3-buku locales extras
Requires:       python3-buku = %{version}-%{release}
Provides:       python3dist(buku[locales]) = %{version}-%{release}

%description -n python3-buku+locales
Metapackage for python3-buku locales extras.

%description
Buku is a powerful bookmark manager written in Python3 and SQLite3.

Buku fetches the title of a bookmarked web page and stores it along
with any additional comments and tags. You can use your favourite editor
to compose and update bookmarks. With multiple search options, including regex
and a deep scan mode (particularly for URLs), it can find any bookmark
instantly. Multiple search results can be opened in the browser at once.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i "s|urllib3>=1.23,<2|urllib3<3|" setup.py

%build

PYTHONPATH=$PWD/build/lib sphinx-build docs/source html
rm -rf html/.{doctrees,buildinfo}
%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/buku-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  auto-completion/fish/buku.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_buku
%py3_shebang_fix %{buildroot}%{_bindir}
%oreon_autofiles main

%files

%changelog

%autochangelog

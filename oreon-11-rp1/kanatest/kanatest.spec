%global source0_hash 88c764f808381a9a5b996e4e8a5246ac43a7822fafd604135474bdf1b5d46f2a
%global git_snapshot 1
%if 0%{?git_snapshot}
%global git_rev  19dd1a7df9e1cd1c72a47b091ffeac5c0eabb354
%global git_date 20170810
%global git_short %(echo %{git_rev} | cut -c-8)
%global git_version D%{git_date}git%{git_short}
%endif
%global mainver 0.4.10
%global mainrel 0.1
Name:           kanatest
Version:        %{mainver}
Release:        1%{?dist}
Summary:        Hiragana and Katakana drill tool
License:        GPL-2.0-or-later
URL:            http://clayo.org/kanatest/
%if 0%{?git_snapshot}
Source0:        %{name}-%{version}-D%{git_date}git%{git_short}.tar.bz2
%else
%endif
Source100:      create-tarball-from-git.sh
%if 0%{?git_snapshot}
%endif
Requires:       font(:lang=ja)
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%description
Kanatest is a simple, GTK 2-based kana drill tool. It offers three drill modes:
hiragana, katakana, and mixed mode. The tester shows random kana characters
and waits until you enter the romaji equivalent in an entry field. At the end,
statistics are provided

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q %{?git_version:-n %{name}-%{version}-%{?git_version}}

sed -i \
	src/Makefile.in \
%if 0%{?git_snapshot}
	src/Makefile.am \
%endif
	-e 's|DISABLE_DEPRECATED|ENABLE_DEPRECATED|g'

%build

%if 0%{?git_snapshot}
bash autogen.sh
%endif
export PLATFORM_CFLAGS="$RPM_OPT_FLAGS -Werror-implicit-function-declaration"
%configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

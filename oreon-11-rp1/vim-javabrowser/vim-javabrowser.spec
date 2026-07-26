%global source0_hash ec368548eb6f77e13e72353709bcc1ce76b74a81eb0f56a83eecee5e6b50be42

%global baseversion 2.03
%global zipname JavaBrowser
%global pkgname javabrowser
#used for pre-releases:
%global vimfiles_root %{_datadir}/vim/vimfiles

Summary:     The javabrowser plugin for VIM editor
Name:        vim-%{pkgname}
Version:     %{baseversion}
Release:     27%{?dist}

License:     Vim
URL:         http://www.vim.org/scripts/script.php?script_id=588
Source:      http://github.com/vim-scripts/JavaBrowser/archive/2.03.zip
Source1:     vim-javabrowser.metainfo.xml

Requires:    vim-common
BuildArch:   noarch

%description
This script is SPECIFICALLY tailored for Java language.
So, it shows structure of the Java file starting with classes defined within it
and NOT in a general tag structure.
It also has a nice syntax to show the class members in UML format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{zipname}-%{baseversion}

%build

%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar plugin %{buildroot}%{vimfiles_root}
cp -ar pixmaps %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_datadir}/appdata
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata

%files 
%doc README
%{vimfiles_root}/plugin/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
%autochangelog

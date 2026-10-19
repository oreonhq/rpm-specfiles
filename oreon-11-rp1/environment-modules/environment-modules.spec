%global source0_hash 3e3cc7582ea34f3cf8353152fae724dea00dc893f021080263f475dcaeb40520
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
Name:           environment-modules
Version:        5.7.0
Release:        1%{?dist}
Summary:        Provides dynamic modification of a user's environment
License:        GPL-2.0-or-later
URL:            https://envmodules.io
Source0:        https://downloads.sourceforge.net/modules/modules-%{version}.tar.bz2
Requires:       tcl
Requires:       sed
Requires:       less
Requires:       util-linux-core
Requires:       vim-filesystem
Requires:       emacs-filesystem%{?_emacs_version: >= %{_emacs_version}}
Requires:       procps-ng
Requires:       man-db
Requires(post): coreutils
Requires(post): %{_bindir}/update-alternatives
Requires(postun): %{_bindir}/update-alternatives
Provides:       environment(modules)
Obsoletes:      environment-modules-compat <= 4.8.99
# oreon:deps
BuildRequires:  dejagnu
BuildRequires:  emacs-nw
BuildRequires:  gcc
BuildRequires:  hostname
BuildRequires:  less
BuildRequires:  make
BuildRequires:  procps-ng
BuildRequires:  sed
BuildRequires:  tcl
BuildRequires:  tcl-devel
BuildRequires:  util-linux-core
BuildRequires:  vim-filesystem
# /oreon:deps
%description
The Environment Modules package provides for the dynamic modification of
a user's environment via modulefiles.

Each modulefile contains the information needed to configure the shell
for an application. Once the Modules package is initialized, the
environment can be modified on a per-module basis using the module
command which interprets modulefiles. Typically modulefiles instruct
the module command to alter or set shell environment variables such as
PATH, MANPATH, etc. modulefiles may be shared by many users on a system
and users may have their own collection to supplement or replace the
shared modulefiles.

Modules can be loaded and unloaded dynamically and atomically, in an
clean fashion. All popular shells are supported, including bash, ksh,
zsh, sh, csh, tcsh, as well as some scripting languages such as perl.

Modules are useful in managing different versions of applications.
Modules can also be bundled into meta-modules that will load an entire
suite of different applications.

NOTE: You will need to get a new shell after installing this package to
have access to the module alias.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n modules-%{version}

%build

%configure --prefix=%{_datadir}/Modules \
           --libdir=%{_libdir}/%{name} \
           --etcdir=%{_sysconfdir}/%{name} \
           --bindir=%{_datadir}/Modules/bin \
           --libexecdir=%{_datadir}/Modules/libexec \
           --mandir=%{_mandir} \
           --vimdatadir=%{vimfiles_root} \
           --emacsdatadir=%{_emacs_sitelispdir}/%{name} \
           --nagelfardatadir=%{_datadir}/Modules/nagelfar \
           --with-bashcompletiondir=%{bash_completions_dir} \
           --with-fishcompletiondir=%{fish_completions_dir} \
           --with-zshcompletiondir=%{zsh_completions_dir} \
           --enable-multilib-support \
           --disable-doc-install \
           --enable-modulespath \
           --with-python=/usr/bin/python3 \
           --with-modulepath=%{_datadir}/Modules/modulefiles:%{_sysconfdir}/modulefiles:%{_datadir}/modulefiles \
           --with-quarantine-vars='LD_LIBRARY_PATH LD_PRELOAD'
%make_build
%{_emacs_bytecompile} share/emacs/lisp/modulefile-mode.el
%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/modulefiles
mkdir -p %{buildroot}%{_datadir}/modulefiles
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_datadir}/fish/vendor_conf.d
mkdir -p %{buildroot}%{_bindir}
touch %{buildroot}%{_sysconfdir}/profile.d/modules.{csh,sh}
touch %{buildroot}%{_datadir}/fish/vendor_conf.d/modules.fish
touch %{buildroot}%{_bindir}/modulecmd
rm -f %{buildroot}%{_datadir}/Modules/bin/modulecmd
mv %{buildroot}%{_datadir}/Modules/bin/envml %{buildroot}%{_bindir}/
mv {doc/build/,}NEWS.txt
mv {doc/build/,}MIGRATING.txt
mv {doc/build/,}CONTRIBUTING.txt
mv {doc/build/,}INSTALL.txt
mv {doc/build/,}changes.txt
install -Dpm 644 share/rpm/macros.%{name} %{buildroot}/%{macrosdir}/macros.%{name}
install -Dpm 644 share/emacs/lisp/%{name}-init.el %{buildroot}/%{_emacs_sitestartdir}/%{name}-init.el
%oreon_autofiles main

%check

make test QUICKTEST=1
%post

[ ! -L %{_sysconfdir}/profile.d/modules.sh ] &&  rm -f %{_sysconfdir}/profile.d/modules.sh
[ ! -L %{_sysconfdir}/profile.d/modules.csh ] &&  rm -f %{_sysconfdir}/profile.d/modules.csh
[ ! -L %{_datadir}/fish/vendor_conf.d/modules.fish ] &&  rm -f %{_datadir}/fish/vendor_conf.d/modules.fish
[ ! -L %{_bindir}/modulecmd ] &&  rm -f %{_bindir}/modulecmd
if [ "$(readlink /etc/alternatives/modules.sh)" = '%{_datadir}/Modules/init/modules.sh' ]; then
  update-alternatives --remove modules.sh %{_datadir}/Modules/init/modules.sh
fi
update-alternatives \
  --install %{_sysconfdir}/profile.d/modules.sh modules.sh %{_datadir}/Modules/init/profile.sh 40 \
  --follower %{_sysconfdir}/profile.d/modules.csh modules.csh %{_datadir}/Modules/init/profile.csh \
  --follower %{_datadir}/fish/vendor_conf.d/modules.fish modules.fish %{_datadir}/Modules/init/fish \
  --follower %{_bindir}/modulecmd modulecmd %{_datadir}/Modules/libexec/modulecmd.tcl
%postun

if [ $1 -eq 0 ] ; then
  update-alternatives --remove modules.sh %{_datadir}/Modules/init/profile.sh
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

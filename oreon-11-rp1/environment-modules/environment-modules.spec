%global source0_hash 5d36fd90b83a06fd3ed0ff951ab1101f22eb310fde3492f9d0455a68569abe5b

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           environment-modules
Version:        5.6.1
Release:        3%{?dist}
Summary:        Provides dynamic modification of a user's environment

License:        GPL-2.0-or-later
URL:            https://envmodules.io
Source0:        https://downloads.sourceforge.net/modules/modules-%{version}.tar.bz2

BuildRequires:  tcl
BuildRequires:  dejagnu
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  less
BuildRequires:  util-linux-core
BuildRequires:  hostname
BuildRequires:  procps-ng
# specific requirements to build extension library
BuildRequires:  gcc
BuildRequires:  tcl-devel
Requires:       tcl
Requires:       sed
Requires:       less
Requires:       util-linux-core
BuildRequires:  vim-filesystem
Requires:       vim-filesystem
BuildRequires:  emacs-nw
Requires:       emacs-filesystem%{?_emacs_version: >= %{_emacs_version}}
Requires:       procps-ng
Requires:       man-db
Requires(post): coreutils
Requires(post): %{_bindir}/update-alternatives
Requires(postun): %{_bindir}/update-alternatives
Provides:       environment(modules)
Obsoletes:      environment-modules-compat <= 4.8.99

%if 0%{?fedora}
# Tcl linter is useful for module lint command
Recommends:     nagelfar
%endif

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

# compile Elisp file
%{_emacs_bytecompile} share/emacs/lisp/modulefile-mode.el


%install
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/modulefiles
mkdir -p %{buildroot}%{_datadir}/modulefiles
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_datadir}/fish/vendor_conf.d
mkdir -p %{buildroot}%{_bindir}

# setup for alternatives
touch %{buildroot}%{_sysconfdir}/profile.d/modules.{csh,sh}
touch %{buildroot}%{_datadir}/fish/vendor_conf.d/modules.fish
touch %{buildroot}%{_bindir}/modulecmd
# remove modulecmd wrapper as it will be handled by alternatives
rm -f %{buildroot}%{_datadir}/Modules/bin/modulecmd

# major utilities go to regular bin dir
mv %{buildroot}%{_datadir}/Modules/bin/envml %{buildroot}%{_bindir}/

mv {doc/build/,}NEWS.txt
mv {doc/build/,}MIGRATING.txt
mv {doc/build/,}CONTRIBUTING.txt
mv {doc/build/,}INSTALL.txt
mv {doc/build/,}changes.txt

# install the rpm config file
install -Dpm 644 share/rpm/macros.%{name} %{buildroot}/%{macrosdir}/macros.%{name}

# install Emacs init file
install -Dpm 644 share/emacs/lisp/%{name}-init.el %{buildroot}/%{_emacs_sitestartdir}/%{name}-init.el


%check
make test QUICKTEST=1


%post
# Cleanup from pre-alternatives
[ ! -L %{_sysconfdir}/profile.d/modules.sh ] &&  rm -f %{_sysconfdir}/profile.d/modules.sh
[ ! -L %{_sysconfdir}/profile.d/modules.csh ] &&  rm -f %{_sysconfdir}/profile.d/modules.csh
[ ! -L %{_datadir}/fish/vendor_conf.d/modules.fish ] &&  rm -f %{_datadir}/fish/vendor_conf.d/modules.fish
[ ! -L %{_bindir}/modulecmd ] &&  rm -f %{_bindir}/modulecmd

# Migration from version 3.x to 4
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


%files
%license COPYING.GPLv2
%doc ChangeLog.gz README NEWS.txt MIGRATING.txt INSTALL.txt CONTRIBUTING.txt changes.txt
%{_sysconfdir}/modulefiles
%dir %{_datadir}/fish/vendor_conf.d
%ghost %{_sysconfdir}/profile.d/modules.csh
%ghost %{_sysconfdir}/profile.d/modules.sh
%ghost %{_datadir}/fish/vendor_conf.d/modules.fish
%ghost %{_bindir}/modulecmd
%{_bindir}/envml
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libtclenvmodules.so
%dir %{_datadir}/Modules
%{_datadir}/Modules/bin
%dir %{_datadir}/Modules/libexec
%{_datadir}/Modules/libexec/modulecmd.tcl
%dir %{_datadir}/Modules/init
%{_datadir}/Modules/init/*
# do not need to require shell package as we "own" completion dir
%dir %{bash_completions_dir}
%{bash_completions_dir}/module
%{bash_completions_dir}/ml
%dir %{zsh_completions_dir}
%{zsh_completions_dir}/_module
%dir %{fish_completions_dir}
%{fish_completions_dir}/module.fish
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/initrc
%config(noreplace) %{_sysconfdir}/%{name}/modulespath
%config(noreplace) %{_sysconfdir}/%{name}/siteconfig.tcl
%{_datadir}/Modules/modulefiles
%{_datadir}/modulefiles
%{_mandir}/man1/envml.1.gz
%{_mandir}/man1/ml.1.gz
%{_mandir}/man1/module.1.gz
%{_mandir}/man5/modulefile.5.gz
%{macrosdir}/macros.%{name}
%{vimfiles_root}/ftdetect/modulefile.vim
%{vimfiles_root}/ftplugin/modulefile.vim
%{vimfiles_root}/syntax/modulefile.vim
%dir %{_emacs_sitelispdir}/%{name}
%{_emacs_sitelispdir}/%{name}/*
%{_emacs_sitestartdir}/%{name}-init.el
%dir %{_datadir}/Modules/nagelfar
%{_datadir}/Modules/nagelfar/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.6.1-3
- Prepare for Oreon 11 (RP1)

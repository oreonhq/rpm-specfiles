%global source0_hash e284c0e6b3fe0a0cd6be67df71dfbf6aa321188973db683a057f5637552fbc8c

%global srcname ClusterShell
%global vimdatadir %{_datadir}/vim/vimfiles

Name:           clustershell
Version:        1.9.3
Release:        8%{?dist}
Summary:        Python framework for efficient cluster administration

License:        LGPL-2.1-or-later
URL:            https://cea-hpc.github.io/clustershell/
Source0:        https://files.pythonhosted.org/packages/source/C/%{srcname}/%{srcname}-%{version}.tar.gz#/%{srcname}-%{version}.pypi.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  vim

Requires:       python3-%{name} = %{version}-%{release}
Requires:       vim-filesystem
Provides:       vim-clustershell = %{version}-%{release}
Obsoletes:      vim-clustershell < 1.7.81-4

%description
ClusterShell is a set of tools and a Python library to execute commands
on cluster nodes in parallel depending on selected engine and worker
mechanisms. Advanced node sets and node groups handling methods are provided
to ease and improve the daily administration of large compute clusters or
server farms. Command line utilities like clush, clubak and nodeset (or
cluset) allow traditional shell scripts to take benefit of the features
offered by the library.

%package -n python3-%{name}
Summary:        ClusterShell module for Python 3
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
ClusterShell Python 3 module and related command line tools.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

# move config dir away from default setuptools /usr prefix (if rpm-building as user)
[ -d %{buildroot}/usr/etc ] && mv %{buildroot}/usr/etc %{buildroot}/%{_sysconfdir}

# man pages
install -d %{buildroot}/%{_mandir}/{man1,man5}
install -p -m 0644 doc/man/man1/clubak.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/cluset.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/clush.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man1/nodeset.1 %{buildroot}/%{_mandir}/man1/
install -p -m 0644 doc/man/man5/clush.conf.5 %{buildroot}/%{_mandir}/man5/
install -p -m 0644 doc/man/man5/groups.conf.5 %{buildroot}/%{_mandir}/man5/

# vim addons
install -d %{buildroot}/%{vimdatadir}/{ftdetect,syntax}
install -p -m 0644 doc/extras/vim/ftdetect/clustershell.vim %{buildroot}/%{vimdatadir}/ftdetect/
install -p -m 0644 doc/extras/vim/syntax/clushconf.vim %{buildroot}/%{vimdatadir}/syntax/
install -p -m 0644 doc/extras/vim/syntax/groupsconf.vim %{buildroot}/%{vimdatadir}/syntax/

install -d %{buildroot}%{bash_completions_dir}
install -p -m 0644 bash_completion.d/cluset -t %{buildroot}%{bash_completions_dir}
install -p -m 0644 bash_completion.d/clush -t %{buildroot}%{bash_completions_dir}
pushd %{buildroot}%{bash_completions_dir}
ln -s cluset nodeset
popd

%files -n python3-%{name} -f %{pyproject_files}
%{_bindir}/clubak
%{_bindir}/cluset
%{_bindir}/clush
%{_bindir}/nodeset

%files
%doc ChangeLog COPYING.LGPLv2.1 README.md
%doc doc/examples
%doc doc/sphinx
%{_mandir}/man1/clubak.1*
%{_mandir}/man1/cluset.1*
%{_mandir}/man1/clush.1*
%{_mandir}/man1/nodeset.1*
%{_mandir}/man5/clush.conf.5*
%{_mandir}/man5/groups.conf.5*
%dir %{_sysconfdir}/clustershell
%dir %{_sysconfdir}/clustershell/clush.conf.d
%dir %{_sysconfdir}/clustershell/groups.d
%dir %{_sysconfdir}/clustershell/groups.conf.d
%config(noreplace) %{_sysconfdir}/clustershell/clush.conf
%config(noreplace) %{_sysconfdir}/clustershell/groups.conf
%ghost %{_sysconfdir}/clustershell/groups
%config(noreplace) %{_sysconfdir}/clustershell/groups.d/local.cfg
%doc %{_sysconfdir}/clustershell/clush.conf.d/README
%doc %{_sysconfdir}/clustershell/clush.conf.d/*.conf.example
%doc %{_sysconfdir}/clustershell/groups.conf.d/README
%doc %{_sysconfdir}/clustershell/groups.conf.d/*.conf.example
%doc %{_sysconfdir}/clustershell/groups.d/README
%doc %{_sysconfdir}/clustershell/groups.d/*.yaml.example
%doc %{_sysconfdir}/clustershell/topology.conf.example
%{vimdatadir}/ftdetect/clustershell.vim
%{vimdatadir}/syntax/clushconf.vim
%{vimdatadir}/syntax/groupsconf.vim
%{bash_completions_dir}/cluset
%{bash_completions_dir}/clush
%{bash_completions_dir}/nodeset

%changelog
%autochangelog

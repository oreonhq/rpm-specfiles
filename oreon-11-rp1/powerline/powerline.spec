%global source0_hash 9e846af9379b57e410efe264cff3a6b98eb78dd9526e83016776ae5ffc5798f4
Name:           powerline
Version:        2.8.4
Release:        1%{?dist}
Summary:        The ultimate status-line/prompt utility
License:        MIT
Url:            https://github.com/powerline/powerline
Requires:       python3
Requires:       powerline-fonts
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Recommends:     python3-pygit2
Source0:        https://github.com/powerline/powerline/archive/%{version}/powerline-%{version}.tar.gz
Source1:        vim-powerline.metainfo.xml
Patch0:         0001-Fix-TypeError-bad-argument-type-for-built-in-operati.patch
Patch1:         0002-Rename-assertion-method.patch
Patch2:         0003-Fix-compatibility-with-Python-3.14.patch
Patch3:         0004-Fix-compatibility-with-Python-3.15.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-powerline = %{version}-%{release}
# /oreon:deps
%description
Powerline is a status-line plugin for vim, and provides status-lines and prompts
for several other applications, including zsh, bash, tmux, IPython, Awesome and
Qtile.

%package docs
Summary: Powerline Documentation
BuildArch: noarch
%description docs
This package provides the powerline documentation.

%package fonts
Summary: Powerline symbol font
BuildArch: noarch
Requires: fontpackages-filesystem
%description fonts
This package provides the symbol font used by Powerline, plus a fontconfig file
that allows using these symbols as part of common monospaced fonts.

%package -n vim-powerline
Summary: Powerline VIM plugin
BuildArch: noarch
Requires: vim
Requires: %{name} = %{version}-%{release}
Obsoletes: vim-plugin-powerline < %{version}-%{release}
Provides: vim-plugin-powerline = %{version}-%{release}
%description -n vim-powerline
Powerline is a status-line plugin for vim, and provides status-lines and
prompts.

%package -n tmux-powerline
Summary: Powerline for tmux
BuildArch: noarch
Requires: tmux
Requires: %{name} = %{version}-%{release}
%description -n tmux-powerline
Powerline for tmux.

Add

    source /usr/share/tmux/powerline.conf

to your ~/.tmux.conf file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
find -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build

sed -i -e "/DEFAULT_SYSTEM_CONFIG_DIR/ s@None@'%{_sysconfdir}/xdg'@" powerline/config.py
sed -i -e "/TMUX_CONFIG_DIRECTORY/ s@BINDINGS_DIRECTORY@'/usr/share'@" powerline/config.py
CFLAGS="%{build_cflags} %{build_ldflags}" \
%pyproject_wheel
%install
%pyproject_install
ldd %{buildroot}%{_bindir}/powerline
pushd docs
%__make html SPHINXBUILD=/usr/bin/sphinx-build-3
%__rm _build/html/.buildinfo
sed -i -e 's/abuild/user/g' _build/html/develop/extensions.html
%__make man SPHINXBUILD=/usr/bin/sphinx-build-3
popd
install -d -m0755 %{buildroot}%{_sysconfdir}/xdg/%{name}
cp -a powerline/config_files/* %{buildroot}%{_sysconfdir}/xdg/%{name}/
install -d -m0755 %{buildroot}%{_sysconfdir}/fonts/conf.d
install -d -m0755 %{buildroot}%{_datadir}/fonts/truetype
install -d -m0755 %{buildroot}%{_datadir}/fontconfig/conf.avail
install -m0644 font/PowerlineSymbols.otf %{buildroot}%{_datadir}/fonts/truetype/PowerlineSymbols.otf
install -m0644 font/10-powerline-symbols.conf %{buildroot}%{_datadir}/fontconfig/conf.avail/10-powerline-symbols.conf
ln -sr %{buildroot}%{_datadir}/fontconfig/conf.avail/10-powerline-symbols.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/10-powerline-symbols.conf
%__install -d -m0755 %{buildroot}%{_datadir}/man/man1
for f in powerline-config.1 powerline-daemon.1 powerline-lint.1 powerline.1; do
%__install -m0644 docs/_build/man/$f %{buildroot}%{_datadir}/man/man1/$f
done
install -d -m0755 %{buildroot}%{_datadir}/%{name}
for binding in awesome bash fish i3 qtile shell tcsh zsh; do
  mv %{buildroot}%{python3_sitelib}/%{name}/bindings/"$binding" %{buildroot}%{_datadir}/%{name}/
done
sed -i '1{\@^#!/usr/bin/python3@d}' %{buildroot}%{python3_sitelib}/%{name}/bindings/pdb/__main__.py
install -d -m0755 %{buildroot}%{_datadir}/tmux
mv %{buildroot}%{python3_sitelib}/powerline/bindings/tmux/powerline*.conf %{buildroot}%{_datadir}/tmux/
install -d -m0755 %{buildroot}%{_datadir}/vim/vimfiles/plugin/
mv %{buildroot}%{python3_sitelib}/powerline/bindings/vim/plugin/powerline.vim %{buildroot}%{_datadir}/vim/vimfiles/plugin/powerline.vim
rm -rf %{buildroot}%{python3_sitelib}/powerline/bindings/vim/plugin
install -d -m0755 %{buildroot}%{_datadir}/vim/vimfiles/autoload/powerline
mv %{buildroot}%{python3_sitelib}/powerline/bindings/vim/autoload/powerline/debug.vim %{buildroot}%{_datadir}/vim/vimfiles/autoload/powerline/debug.vim
rm -rf %{buildroot}%{python3_sitelib}/powerline/bindings/vim/autoload
mkdir -p %{buildroot}%{_datadir}/metainfo
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo
install -d -m 0755 %{buildroot}%{_userunitdir}
mv %{buildroot}%{python3_sitelib}/%{name}/dist/systemd/powerline-daemon.service %{buildroot}%{_userunitdir}/powerline.service
%__rm -rf %{buildroot}%{python3_sitelib}/%{name}/config_files
%__rm -rf %{buildroot}%{python3_sitelib}/%{name}/dist
%oreon_autofiles vim-powerline usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles tmux-powerline usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

PYTHONPATH=. TEST_ROOT=. \
%pytest -r s -k 'not (test_kw_threaded_segment or test_logger_format or test_system_load or test_threaded_segment or test_top_log_format or test_user)'
%post

%systemd_user_post powerline.service
%preun

%systemd_user_preun powerline.service
%postun

%systemd_user_postun_with_restart powerline.service
%files
%files -n powerline-docs -f %{oreon_filedir}/powerline-docs.list
%files -n powerline-fonts -f %{oreon_filedir}/powerline-fonts.list
%files -n vim-powerline -f %{oreon_filedir}/vim-powerline.list
%files -n tmux-powerline -f %{oreon_filedir}/tmux-powerline.list

%changelog

%autochangelog

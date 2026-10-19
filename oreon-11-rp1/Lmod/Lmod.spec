%global source0_hash 30c9e29d6ab942a194e9c8f7c78430f4e26269d9439a68f451fe1ca4063da774
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global debug_package %{nil}
Name:           Lmod
Version:        9.4.2
Release:        1%{?dist}
Summary:        Environmental Modules System in Lua
License:        MIT AND LGPL-2.0-only
URL:            https://tacc.utexas.edu/research/tacc-research/lmod/
Source0:        https://github.com/TACC/Lmod/archive/%{version}/Lmod-%{version}.tar.gz
Source1:        macros.%{name}
Requires:       lua-filesystem
Requires:       lua-json
Requires:       lua-posix
Requires:       lua-term
Requires:       /usr/bin/ps
Provides:       environment(modules)
# oreon:deps
BuildRequires:  bc
BuildRequires:  gcc
BuildRequires:  lua-devel
BuildRequires:  lua-filesystem
BuildRequires:  lua-json
BuildRequires:  lua-posix
BuildRequires:  lua-term
BuildRequires:  make
BuildRequires:  tcl-devel
BuildRequires:  zsh
# /oreon:deps
%description
Lmod is a Lua based module system that easily handles the MODULEPATH
Hierarchical problem.  Environment Modules provide a convenient way to
dynamically change the users' environment through modulefiles. This includes
easily adding or removing directories to the PATH environment variable.
Modulefiles for library packages provide environment variables that specify
where the library and header files can be found.

%prep

%autosetup -p1
sed -i -e 's,/usr/bin/env ,/usr/bin/,' src/*.tcl
# Remove bundled lua-filesystem and lua-term
rm -r pkgs/{luafilesystem,term} tools/json.lua
#sed -i -e 's, pkgs , ,' Makefile.in
# Remove unneeded shbangs
sed -i -e '/^#!/d' init/*.in

%build

%configure --prefix=%{_datadir} PS=/usr/bin/ps
%make_build
%install
%set_build_flags
%make_install
find %{buildroot}%{_datadir}/lmod/%{version}/init -type f -exec chmod -x {} +
mkdir -p %{buildroot}%{_sysconfdir}/modulefiles
mkdir -p %{buildroot}%{_datadir}/modulefiles
mkdir -p %{buildroot}%{_sysconfdir}/profile.d %{buildroot}%{_datadir}/fish/vendor_conf.d
cat <<'EOF' > %{buildroot}%{_sysconfdir}/profile.d/00-modulepath.sh
[ -z "$MODULEPATH" ] &&
  [ "$(readlink /etc/alternatives/modules.sh)" = "/usr/share/lmod/lmod/init/profile" -o -f /etc/profile.d/z00_lmod.sh ] &&
  export MODULEPATH=%{_sysconfdir}/modulefiles:%{_datadir}/modulefiles || :
EOF
cat << 'EOF' > %{buildroot}%{_sysconfdir}/profile.d/00-modulepath.csh
if (! $?MODULEPATH && ( `readlink /etc/alternatives/modules.csh` == /usr/share/lmod/lmod/init/cshrc || -f /etc/profile.d/z00_lmod.csh ) ) then
  setenv MODULEPATH %{_sysconfdir}/modulefiles:%{_datadir}/modulefiles
endif
EOF
sed -i '2i\. /etc/profile.d/00-modulepath.sh\n' \
  %{buildroot}%{_datadir}/lmod/lmod/init/profile
install -Dpm 644 %{SOURCE1} %{buildroot}/%{macrosdir}/macros.%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

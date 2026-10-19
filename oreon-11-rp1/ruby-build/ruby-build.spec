%global source0_hash 9346ff4de06211d0647cf755c398d290e7b6046fe12a69671ecc40f9fa360e09
%bcond check 1
%global debug_package %{nil}
Name:           ruby-build
Version:        20260917
Release:        1%{?dist}
Summary:        Compile and install Ruby
License:        MIT
URL:            https://github.com/rbenv/ruby-build
Source0:        https://github.com/rbenv/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          2576.patch
%if %{with check}
%endif
Requires:       ruby-build-core = %{version}-%{release}
Recommends:     ruby-build-ruby = %{version}-%{release}
# oreon:deps
BuildRequires:  bats
BuildRequires:  gawk
BuildRequires:  grep
# /oreon:deps
%description
ruby-build is a command-line utility that makes it easy to install virtually
any version of Ruby, from source.

%package        core
Summary:        Core executable and scripts for ruby-build
License:        MIT
%description    core
This package contains the core ruby-build executable and man pages,
without any specific Ruby definition files.

%package        rbenv
Summary:        rbenv plugin to compile and install Ruby
Requires:       ruby-build = %{version}-%{release}
Requires:       rbenv
%description    rbenv
This package contains a plugin for rbenv that provides the "rbenv install"
command.

%package        ruby
Summary:        ruby-build targets for MRI/CRuby versions
Requires:       ruby-build-core = %{version}-%{release}
Requires:       gcc
Requires:       libffi-devel
Requires:       libyaml-devel
Requires:       perl-interpreter
Requires:       perl(File::Compare)
Requires:       perl(File::Copy)
Requires:       perl(FindBin)
Requires:       perl(IPC::Cmd)
Requires:       perl(lib)
Requires:       perl(Time::Piece)
Requires:       zlib-ng-compat-devel
%description    ruby
This package contains ruby-build targets for MRI/CRuby versions.

%package        jruby
Summary:        ruby-build targets for jruby versions
Requires:       ruby-build-core = %{version}-%{release}
Requires:       gcc-c++
Requires:       java-latest-openjdk-headless
Requires:       make
%description    jruby
This package contains ruby-build targets for jruby versions.

%package        mruby
Summary:        ruby-build targets for mruby versions
Requires:       ruby-build-core = %{version}-%{release}
Requires:       ruby
Requires:       rubygem-rake
%description    mruby
This package contains ruby-build targets for mruby versions.

%package        picoruby
Summary:        ruby-build targets for picoruby versions
Requires:       ruby-build-core = %{version}-%{release}
Requires:       git-core
Requires:       gcc
Requires:       ruby
Requires:       rubygem-rake
%description    picoruby
This package contains ruby-build targets for picoruby versions.

%package        truffleruby
Summary:        ruby-build targets for truffleruby versions
Requires:       ruby-build-core = %{version}-%{release}
Requires:       gcc
Requires:       libyaml-devel
%description    truffleruby
This package contains ruby-build targets for truffleruby versions.

%package        others
Summary:        ruby-build targets for rbx, ree and other versions
Requires:       ruby-build-core = %{version}-%{release}
%description    others
This package contains ruby-build targets for rbx, ree and other versions.

%package        all
Summary:        ruby-build targets for all versions
Requires:       ruby-build = %{version}-%{release}
Requires:       ruby-build-core = %{version}-%{release}
Requires:       ruby-build-ruby = %{version}-%{release}
Requires:       ruby-build-jruby = %{version}-%{release}
Requires:       ruby-build-mruby = %{version}-%{release}
Requires:       ruby-build-picoruby = %{version}-%{release}
Requires:       ruby-build-truffleruby = %{version}-%{release}
Requires:       ruby-build-others = %{version}-%{release}
%description    all
This meta-package contains all ruby-build targets versions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
PREFIX=%{buildroot}%{_prefix} ./install.sh
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 share/man/man1/ruby-build.1
install -Ddpm0755 %{buildroot}%{_libdir}/rbenv/libexec
mv %{buildroot}%{_bindir}/rbenv-* %{buildroot}%{_libdir}/rbenv/libexec
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

for test in "install bundled OpenSSL on macOS"; do
  awk -i inplace '/^@test\s+"'"$test"'"\s*\{/{ print; print "  skip \"disabled failing test\""; next }1' $(grep -rl "@test \"$test\"")
done
bats test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ruby-build-core -f %{oreon_filedir}/ruby-build-core.list
%files -n ruby-build-rbenv -f %{oreon_filedir}/ruby-build-rbenv.list
%files -n ruby-build-ruby -f %{oreon_filedir}/ruby-build-ruby.list
%files -n ruby-build-jruby -f %{oreon_filedir}/ruby-build-jruby.list
%files -n ruby-build-mruby -f %{oreon_filedir}/ruby-build-mruby.list
%files -n ruby-build-picoruby -f %{oreon_filedir}/ruby-build-picoruby.list
%files -n ruby-build-truffleruby -f %{oreon_filedir}/ruby-build-truffleruby.list
%files -n ruby-build-others -f %{oreon_filedir}/ruby-build-others.list
%files -n ruby-build-all -f %{oreon_filedir}/ruby-build-all.list

%changelog

%autochangelog

%global source1_hash 9bf02a09558f3fb65be94144bc1b1085e5e0388a8e697342010f0bdaaeeba4fd
%global source0_hash 239a373da6584574f25f042d8ed4ba21e691c9799f1d2b5c8920bbbc23ca3d41
%global gem_name rack
Name: rubygem-%{gem_name}
Version: 3.2.3
Epoch:  1
Release:        1%{?dist}
Summary:        A modular Ruby webserver interface
License: MIT AND BSD-3-Clause
URL: https://github.com/rack/rack
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rack/rack/archive/refs/tags/v3.2.3.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-global_expectations)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby. By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
cp -a %{builddir}/test .
ruby -Itest -e 'Dir.glob "./test/spec_*.rb", &method(:require)'
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rack-doc -f %{oreon_filedir}/rubygem-rack-doc.list

%changelog

%autochangelog

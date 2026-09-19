%global source0_hash 239a373da6584574f25f042d8ed4ba21e691c9799f1d2b5c8920bbbc23ca3d41

%global gem_name rack

Name: rubygem-%{gem_name}
Version: 3.2.3
# Introduce Epoch (related to bug 552972)
Epoch:  1
Release: 5%{?dist}
Summary: A modular Ruby webserver interface
# lib/rack/show_{status,exceptions}.rb contains snippets from Django under BSD license.
License: MIT AND BSD-3-Clause
URL: https://github.com/rack/rack
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rack/rack.git && cd rack/
# git archive -v -o rack-3.2.3-tests.tar.gz v3.2.3 test/
Source1: rack-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.4.0
BuildRequires: rubygem(logger)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(minitest-global_expectations)
BuildArch: noarch

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

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}

cp -a %{builddir}/test .

ruby -Itest -e 'Dir.glob "./test/spec_*.rb", &method(:require)'
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/SPEC.rdoc

%changelog
%autochangelog

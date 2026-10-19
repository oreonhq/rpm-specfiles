%global source0_hash d444910e6aa55480c6bcdc0cdb057626e8a32c054c29e793fa642ba2f155f445
%global gem_name redcarpet
Name:		rubygem-%{gem_name}
Version:	3.6.1
Release:        4%{?dist}
Summary:        A fast, safe and extensible Markdown to (X)HTML parser
License:	MIT
URL:		http://github.com/vmg/redcarpet
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
Source2:	%{gem_name}-create-missing-test-files.sh
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A fast, safe and extensible Markdown to (X)HTML parser.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description	doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
cp -p ../%{gem_name}-%{version}.gemspec .

%build

gem build ./%{gem_name}-%{version}.gemspec
%gem_install
chmod a-x .%{gem_instdir}/ext/redcarpet/html.c
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}
chmod 755 %{buildroot}%{_bindir}/redcarpet
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} \
	%{buildroot}%{gem_extdir_mri}/
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Rakefile \
	ext/ \
	test/ \
	%{gem_name}.gemspec \
	%{nil}
popd
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cp -a test/ .%{gem_instdir}/
pushd .%{gem_instdir}
env \
	RUBYOPT=-Ilib:$(dirs +1)%{gem_extdir_mri}:test \
	ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-redcarpet-doc -f %{oreon_filedir}/rubygem-redcarpet-doc.list

%changelog

%autochangelog

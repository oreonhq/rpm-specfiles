%global source0_hash aae5da8a2bd78901cb87536cc780c47c3f9c542f4ee63e0df47835d6eb75770f
%global gem_name kramdown-syntax-coderay
Name:           rubygem-%{gem_name}
Summary:        Coderay syntax highlighting for kramdown
Version:        1.0.1
Release:        15%{?dist}
License:        MIT
URL:            https://github.com/kramdown/syntax-coderay
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:      noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(coderay)
BuildRequires:  rubygem(kramdown)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
kramdown-syntax-coderay uses coderay to highlight code blocks/spans.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -I'lib' -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-kramdown-syntax-coderay-doc -f %{oreon_filedir}/rubygem-kramdown-syntax-coderay-doc.list

%changelog

%autochangelog

%global source0_hash 1f7b91a7c27ac7d21b1169c3802ef8f482c2aa39122655ddc4772454d55b46d5

%{lua:
if macros.orbs_chain_plan == nil and macros._without_bootstrap == nil then
  local spec
  local cmd = io.open("/proc/self/cmdline", "rb")
  if cmd then
    local data = cmd:read("*a") or ""
    cmd:close()
    local cur = ""
    local function take(arg)
      if string.sub(arg, -5) == ".spec" then spec = arg end
    end
    for i = 1, #data do
      local c = string.sub(data, i, i)
      if string.byte(c) == 0 then
        take(cur)
        cur = ""
      else
        cur = cur .. c
      end
    end
    take(cur)
  end
  local function trim(s)
    local a, b = 1, #s
    while a <= b do
      local c = string.sub(s, a, a)
      if c ~= " " and string.byte(c) ~= 9 then break end
      a = a + 1
    end
    while b >= a do
      local c = string.sub(s, b, b)
      if c ~= " " and string.byte(c) ~= 9 then break end
      b = b - 1
    end
    return string.sub(s, a, b)
  end
  local function miss(dep)
    local p = io.popen("dnf -q install --assumeno '" .. dep .. "' 2>&1")
    if not p then return true end
    local out = p:read("*a") or ""
    p:close()
    if string.find(out, "nothing provides", 1, true) then return true end
    if string.find(out, "No match", 1, true) then return true end
    if string.find(out, "Failed to resolve", 1, true) then return true end
    if string.find(out, "Nothing to do", 1, true) then return false end
    if string.find(out, "Operation aborted", 1, true) then return false end
    if string.find(out, "already installed", 1, true) then return false end
    return true
  end
  if spec then
    local f = io.open(spec, "r")
    if f then
      local depth, in_else, armed = 0, false, false
      for line in f:lines() do
        local s = trim(line)
        if not armed then
          if string.sub(s, 1, 3) == "%%if" and string.find(s, "{with bootstrap}", 1, true) then
            armed = true
            depth = 1
          end
        elseif string.sub(s, 1, 3) == "%%if" then
          depth = depth + 1
        elseif string.sub(s, 1, 6) == "%%endif" then
          depth = depth - 1
          if depth == 0 then break end
        elseif depth == 1 and string.sub(s, 1, 5) == "%%else" then
          in_else = true
        elseif in_else and depth == 1 and string.lower(string.sub(s, 1, 14)) == "buildrequires:" then
          local dep = trim(string.sub(s, 15))
          if dep ~= "" and string.sub(dep, 1, 1) ~= "%%" and miss(dep) then
            rpm.define("_with_bootstrap 1")
            break
          end
        end
      end
      f:close()
    end
  end
end
}
%bcond_with bootstrap

Name:           google-guice
Version:        6.0.0
Release:        %autorelease
Summary:        Lightweight dependency injection framework for Java 5 and above
License:        Apache-2.0
URL:            https://github.com/google/guice
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./create-tarball.sh %%{version}
Source0:        https://github.com/google/guice/archive/refs/tags/6.0.0.tar.gz#/google-guice-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/google/guice/HEAD/create-tarball.sh

BuildRequires:  jurand
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(aopalliance:aopalliance)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif
%if %{without bootstrap}
# xmvn-builddep misses this:
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 6.0.0-27

%description
Put simply, Guice alleviates the need for factories and the use of new
in your Java code. Think of Guice's @Inject as the new new. You will
still need to write factories in some cases, but your code will not
depend directly on them. Your code will be easier to change, unit test
and reuse in other contexts.

Guice embraces Java's type safe nature, especially when it comes to
features introduced in Java 5 such as generics and annotations. You
might think of Guice as filling in missing features for core
Java. Ideally, the language itself would provide most of the same
features, but until such a language comes along, we have Guice.

Guice helps you design better APIs, and the Guice API itself sets a
good example. Guice is not a kitchen sink. We justify each feature
with at least three use cases. When in doubt, we leave it out. We
build general functionality which enables you to extend Guice rather
than adding every feature to the core framework.

%package -n guice-parent
Summary:        Guice parent POM

%description -n guice-parent
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides parent POM for Guice modules.

%package -n guice-assistedinject
Summary:        AssistedInject extension module for Guice

%description -n guice-assistedinject
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides AssistedInject module for Guice.

%package -n guice-extensions
Summary:        Extensions for Guice

%description -n guice-extensions
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides extensions POM for Guice.

%package -n guice-grapher
Summary:        Grapher extension module for Guice

%description -n guice-grapher
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Grapher module for Guice.

%package -n guice-jmx
Summary:        JMX extension module for Guice

%description -n guice-jmx
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides JMX module for Guice.

%package -n guice-jndi
Summary:        JNDI extension module for Guice

%description -n guice-jndi
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides JNDI module for Guice.

%package -n guice-servlet
Summary:        Servlet extension module for Guice

%description -n guice-servlet
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Servlet module for Guice.

%package -n guice-throwingproviders
Summary:        ThrowingProviders extension module for Guice

%description -n guice-throwingproviders
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides ThrowingProviders module for Guice.

%package -n guice-bom
Summary:        Bill of Materials for Guice

%description -n guice-bom
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Bill of Materials module for Guice.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n guice-%{version}

%java_remove_annotations core/src/ \
  -p ^com.google.common.annotations. \
  -p ^com.google.errorprone.annotations. \

# We don't have struts2 in Fedora yet.
%pom_disable_module struts2 extensions
# Android-specific extension
%pom_disable_module dagger-adapter extensions

# Remove additional build profiles, which we don't use anyways
# and which are only pulling additional dependencies.
%pom_xpath_remove "pom:profile[pom:id='guice.with.jarjar']" core

# Fix OSGi metadata due to not using jarjar
%pom_xpath_set "pom:instructions/pom:Import-Package" \
  "!com.google.inject.*,*" core

# Animal sniffer is only causing problems. Disable it for now.
%pom_remove_plugin :animal-sniffer-maven-plugin core
%pom_remove_plugin :animal-sniffer-maven-plugin extensions

%pom_remove_plugin :maven-gpg-plugin

# We don't have the custom doclet used by upstream. Remove
# maven-javadoc-plugin to generate javadocs with default style.
%pom_remove_plugin -r :maven-javadoc-plugin

# remove test dependency to make sure we don't produce requires
# see #1007498
%pom_remove_dep :guava-testlib extensions
%pom_xpath_remove "pom:dependency[pom:classifier='tests']" extensions

%pom_remove_parent

%pom_disable_module persist extensions
%pom_disable_module spring extensions
%pom_disable_module testlib extensions

%pom_add_dep com.google.code.findbugs:jsr305 core

#%pom_remove_dep :aopalliance core
#%pom_remove_dep :asm core
#%pom_remove_dep :cglib core
#%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:configuration"
#%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions"
#%pom_xpath_set "pom:plugin[pom:artifactId='munge-maven-plugin']/pom:executions/pom:execution/pom:phase" generate-sources core
#%pom_xpath_set "pom:plugin[pom:artifactId='munge-maven-plugin']/pom:executions/pom:execution/pom:goals/pom:goal" munge core

#%pom_xpath_inject "pom:dependency[pom:artifactId='guice']" "<scope>provided</scope>" extensions

%mvn_alias :guice :::classes:

%build
#%mvn_alias "com.google.inject.extensions:" "org.sonatype.sisu.inject:"

#%mvn_package :::no_aop: guice
#%mvn_package :guice:jar:{}: __noinstall

%mvn_file  ":guice-{*}"  guice/guice-@1
%mvn_file  ":guice" guice/%{name} %{name}
#%mvn_alias ":guice" "org.sonatype.sisu:sisu-guice"
# Skip tests because of missing dependency guice-testlib
%mvn_build -j -f -s

%install
%mvn_install

%files -f .mfiles-guice

%files -n guice-parent -f .mfiles-guice-parent
%license COPYING

%files -n guice-assistedinject -f .mfiles-guice-assistedinject

%files -n guice-extensions -f .mfiles-extensions-parent

%files -n guice-grapher -f .mfiles-guice-grapher

%files -n guice-jmx -f .mfiles-guice-jmx

%files -n guice-jndi -f .mfiles-guice-jndi

%files -n guice-servlet -f .mfiles-guice-servlet

%files -n guice-throwingproviders -f .mfiles-guice-throwingproviders

%files -n guice-bom -f .mfiles-guice-bom

%changelog
%autochangelog

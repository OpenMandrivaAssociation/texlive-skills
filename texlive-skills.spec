%global tl_name skills
%global tl_revision 56734

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	Create proficiency tests
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/skills
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skills.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skills.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package attempts to make it easy for even a LaTeX novice to prepare
proficiency tests, especially in combination with the exam document
class. Thus, almost all command names are very similar. After defining
skills in the preamble or in an external file, they are declared using
labels, and can optionally be set as global skills. A skills table is
generated to summarize the evaluated competencies and to allow for
writing down the resulting proficiency level. A user's guide attempts to
explain all of the possibilities in a readable way, with many examples.


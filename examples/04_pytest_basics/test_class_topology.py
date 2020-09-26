import pytest
import task_26_1


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Проверка удаления дублей в топологии"""
    top_with_data = task_26_1.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_method__add__(normalized_topology_example):
    """Проверка наличия метода __add__ и его работы"""
    top1 = task_26_1.Topology(normalized_topology_example)
    top1_size_before_add = len(top1.topology)
    top2 = task_26_1.Topology(
        {("R1", "Eth0/4"): ("R7", "Eth0/0"), ("R1", "Eth0/6"): ("R9", "Eth0/0")}
    )
    top2_size_before_add = len(top2.topology)

    top3 = top1 + top2
    assert isinstance(
        top3, task_26_1.Topology
    ), "Метод __add__ должен возвращать новый экземпляр класса Topology"
    assert len(top3.topology) == 8
    assert (
        len(top1.topology) == top1_size_before_add
    ), "После сложения изменился размер первой топологии. Метод __add__ не должен менять исходные топологии"
    assert (
        len(top2.topology) == top2_size_before_add
    ), "После сложения изменился размер второй топологии. Метод __add__ не должен менять исходные топологии"
